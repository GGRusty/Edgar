import requests
import pandas as pd
import datetime


def get_cik(ticker):
    """
    Get the CIK for a given ticker.
    Args:
        ticker (str): The ticker symbol of the company.
    Returns:
        str: The CIK for the company.
    """
    ticker = ticker.upper()
    headers = {"User-Agent": "russ@sunriseanalysis.com"}
    # Get the tickers JSON file
    tickers_json = requests.get(
        "https://www.sec.gov/files/company_tickers.json", headers=headers
    )
    # Create a DataFrame of the tickers
    cik_df = pd.DataFrame.from_dict(tickers_json.json(), orient="index")
    cik_df["cik_str"] = cik_df["cik_str"].astype(str).str.zfill(10)
    # Get the CIK for the given ticker
    cik = cik_df[cik_df["ticker"] == ticker]["cik_str"].values[0]
    return cik


def get_concept_data(ticker, concept, headers):
    cik = get_cik(ticker)
    # Fetches the concept data and converts it into a DataFrame
    concept_url = f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/us-gaap/{concept}.json"
    concept_df = pd.DataFrame.from_dict(requests.get(concept_url, headers=headers).json())
    return concept_df


def get_unit_data(concept_df):
    df = pd.DataFrame.from_dict(concept_df["units"]["USD"])
    for col in ["start", "end", "filed"]:
        df[col] = pd.to_datetime(df[col])
    df["time_delta"] = df["end"] - df["start"]
    df["val"] = df["val"] / 1_000_000
    df.rename(columns={"val": "value(millions)"}, inplace=True)
    return df


def map_to_quarter(end_date, end_month):
    month_diff = (end_date.month - end_month + 9) % 12
    if 0 <= month_diff < 3:
        return 1
    elif 3 <= month_diff < 6:
        return 2
    elif 6 <= month_diff < 9:
        return 3
    else:  # 9, 10, 11
        return 4
    
    
# Define a helper function to fill the quarter column
def fill_quarter(row, df):
    if pd.isnull(row["quarter"]):
        previous_index = row.name - 1
        next_index = row.name + 1 if row.name < len(df) - 1 else row.name

        if previous_index >= 0 and not pd.isnull(df.loc[previous_index, "quarter"]):
            previous_quarter = df.loc[previous_index, "quarter"]
            row["quarter"] = 1 if previous_quarter == 4 else previous_quarter + 1
        elif not pd.isnull(df.loc[next_index, "quarter"]):
            next_quarter = df.loc[next_index, "quarter"]
            row["quarter"] = 4 if next_quarter == 1 else next_quarter - 1
    return row


def find_fiscal_year(date, annual_data):
    for idx, row in annual_data.iterrows():
        if row["start"] <= date <= row["end"]:
            return row["fiscal_year"]

    # If the date is after the end of the last fiscal year in annual_data, return the next fiscal year
    last_fiscal_year_end = annual_data["end"].max()
    if date > last_fiscal_year_end:
        # Extract the last year, increment it by one, and return it as a fiscal year
        last_year = int(annual_data.iloc[-1]["fiscal_year"][2:])
        next_year = last_year + 1
        return "CY" + str(next_year)

    return None


def fill_missing_quarters(df, annual_data):
    # Iterate over each row in the dataframe
    for idx, row in df.iterrows():
        # Check if the value for the quarter is missing
        if pd.isnull(row["value(millions)"]):
            # Check if there are three other quarters in the same fiscal year
            other_quarters = df[
                (df["fiscal_year"] == row["fiscal_year"]) & (df.index != idx)
            ]["value(millions)"]
            if other_quarters.count() == 3:
                # If there are, find the corresponding annual data
                annual_value = annual_data[
                    annual_data["fiscal_year"] == row["fiscal_year"]
                ]["value(millions)"].values[0]
                # Calculate the sum of the other three quarters
                sum_of_quarters = other_quarters.sum()
                # Fill the missing value with the difference
                df.at[idx, "value(millions)"] = annual_value - sum_of_quarters
    return df


def process_data(df):
    annual_data = df[df["time_delta"] > pd.Timedelta(days=350)]
    df = df.drop(annual_data.index)
    annual_data = annual_data.drop_duplicates(subset="value(millions)", keep="last")
    annual_data = annual_data.dropna(subset="frame")
    annual_data = annual_data.drop(
        columns=["time_delta", "filed", "form", "fy", "fp"]
    ).reset_index(drop=True)

    annual_data.rename(columns={"frame": "fiscal_year"}, inplace=True)
    extra_data = df[df["time_delta"] > pd.Timedelta(days=115)]
    df = df.drop(extra_data.index)
    extra_data.reset_index(drop=True, inplace=True)
    df = df.drop_duplicates(subset="value(millions)", keep="last")
    df = df.drop(columns=["time_delta", "filed", "form", "fy", "fp", "accn"])
    df = df.dropna(subset=["frame"])
    df = df.reset_index(drop=True)
    end_month = annual_data.iloc[0]["end"].month 
    df["quarter"] = df["end"].apply(lambda x: map_to_quarter(x, end_month))
    start_year = int(df["frame"].min()[2:6])  # extract start year from the minimum frame
    end_year = int(df["frame"].max()[2:6])  # extract end year from the maximum frame
    frames = [
        f"CY{year}Q{quarter}"
        for year in range(start_year, end_year + 1)
        for quarter in range(1, 5)
    ]
    df_full = pd.DataFrame({"frame": frames})
    # Step 2: Merge the original DataFrame with the new DataFrame
    quarterly_data = pd.merge(df_full, df, how="left", on="frame")

    # Step 3: Sort the DataFrame by frame
    quarterly_data = quarterly_data.sort_values(by="frame").reset_index(drop=True)

    quarterly_data["next_start"] = quarterly_data["start"].shift(-1)
    quarterly_data["prev_end"] = quarterly_data["end"].shift()

    # For missing quarters, set the 'start' date as the day after the end of the previous quarter,
    # and the 'end' date as the day before the start of the next quarter
    quarterly_data.loc[quarterly_data["start"].isna(), "start"] = quarterly_data[
        "prev_end"
    ] + pd.Timedelta(days=1)
    quarterly_data.loc[quarterly_data["end"].isna(), "end"] = quarterly_data["next_start"] - pd.Timedelta(days=1)

    # Drop the 'next_start' and 'prev_end' columns as they are no longer needed
    quarterly_data.drop(["next_start", "prev_end"], axis=1, inplace=True)
    today = datetime.datetime.today()
    # Calculate the start date of the current quarter
    if today.month < 4:
        quarter_start = datetime.datetime(today.year - 1, 12, 1)
    elif today.month < 7:
        quarter_start = datetime.datetime(today.year, 3, 1)
    elif today.month < 10:
        quarter_start = datetime.datetime(today.year, 6, 1)
    else:
        quarter_start = datetime.datetime(today.year, 9, 1)
    # Remove rows where the 'start' date is on or after the start of the current quarter
    quarterly_data = quarterly_data[quarterly_data["start"] < quarter_start]
    # Apply the function to each row in the DataFrame
    quarterly_data = quarterly_data.apply(
        lambda row: fill_quarter(row, quarterly_data), axis=1
    )
    quarterly_data["quarter"] = quarterly_data["quarter"].astype(int)
    # Apply the function to the 'end' column in 'df'
    quarterly_data["fiscal_year"] = quarterly_data["end"].apply(
        find_fiscal_year, args=(annual_data,)
    )
    # Apply the function to the DataFrame
    quarterly_data = fill_missing_quarters(quarterly_data, annual_data)
    quarterly_data = quarterly_data.drop(columns=["frame"])
    # Convert the 'fiscal_year' column to an integer
    quarterly_data["fiscal_year"] = quarterly_data["fiscal_year"].str.replace("CY", "")
    quarterly_data["fiscal_year"] = quarterly_data["fiscal_year"].astype(int)
    annual_data["fiscal_year"] = annual_data["fiscal_year"].str.replace("CY", "")
    annual_data["fiscal_year"] = annual_data["fiscal_year"].astype(int)
    annual_data.set_index("fiscal_year", inplace=True)
    annual_data.drop(columns=["accn"], inplace=True)
    new_annual_order = ["value(millions)", "start", "end"]
    annual_data = annual_data.reindex(columns=new_annual_order)
    quarterly_data = quarterly_data.set_index(["fiscal_year", "quarter"])
    new_merged_order = ["value(millions)", "start", "end"]
    quarterly_data = quarterly_data.reindex(columns=new_merged_order)
    return annual_data, quarterly_data


# Access data for fiscal year 2022, quarter 1
def get_data_point(year, quarter):
    return quarterly_data.loc[(year, quarter)]

headers = {"User-Agent": "russ@sunriseanalysis.com"}

ticker = "AAPL"
concept = "NetIncomeLoss"

concept_df = get_concept_data(ticker, concept, headers)
unit_df = get_unit_data(concept_df)
annual_data, quarterly_data = process_data(unit_df)
data = get_data_point(2022, 4)


print(annual_data)
print(quarterly_data)
print(data)


