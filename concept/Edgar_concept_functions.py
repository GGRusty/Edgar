import requests
import pandas as pd
import numpy as np
import datetime
# not sure if this works yet just done for the night will pick back up tomorrow
# hopefully I can create a class for concept to make it easier to use in the future

headers = {"User-Agent": "russ@sunriseanalysis.com"}
ticker = "AAPL"
concept = "NetIncomeLoss"

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

def get_concept_data(cik, concept):
    # Fetches the concept data and converts it into a DataFrame
    concept_url = f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/us-gaap/{concept}.json"
    concept_df = pd.DataFrame.from_dict(requests.get(concept_url, headers=headers).json())
    return concept_df

def identify_annual_data(df):
    """
    This function identifies the annual data.
    """
    annual_data = df[df["time_delta"] > pd.Timedelta(days=350)]
    return annual_data, df.drop(annual_data.index)


def clean_annual_data(df):
    """
    This function cleans the annual data.
    """
    df = df.drop_duplicates(subset="value(millions)", keep="last")
    df = df.dropna(subset="frame")
    df = df.drop(
        columns=["time_delta", "filed", "form", "fy", "fp"]
    ).reset_index(drop=True)
    return df


def reformat_annual_data(df):
    """
    This function reformats the annual data.
    """
    df.rename(columns={"frame": "fiscal_year"}, inplace=True)
    df["fiscal_year"] = df["fiscal_year"].str.replace("CY", "")
    df["fiscal_year"] = df["fiscal_year"].astype(int)
    df.set_index("fiscal_year", inplace=True)
    df.drop(columns=["accn"], inplace=True)
    new_annual_order = ["value(millions)", "start", "end"]
    df = df.reindex(columns=new_annual_order)
    return df


def process_annual_data(df):
    # Start by converting relevant columns to datetime and renaming 'val' to 'value(millions)'
    for col in ["start", "end", "filed"]:
        df[col] = pd.to_datetime(df[col])
    df["time_delta"] = df["end"] - df["start"]
    df["val"] = df["val"] / 1_000_000
    df.rename(columns={"val": "value(millions)"}, inplace=True)

    # Identify and separate the annual data
    annual_data, df = identify_annual_data(df)

    # Clean the annual data
    annual_data = clean_annual_data(annual_data)

    # Reformat the annual data
    annual_data = reformat_annual_data(annual_data)

    return annual_data, df

    
def generate_full_frames(df):
    # Generates a full list of frames
    start_year = int(df["frame"].min()[2:6])  # extract start year from the minimum frame
    end_year = int(df["frame"].max()[2:6])  # extract end year from the maximum frame
    frames = [
        f"CY{year}Q{quarter}"
        for year in range(start_year, end_year + 1)
        for quarter in range(1, 5)
    ]
    df_full = pd.DataFrame({"frame": frames})
    return df_full

def fill_dates(df):
    df["next_start"] = df["start"].shift(-1)
    df["prev_end"] = df["end"].shift()
    df.loc[df["start"].isna(), "start"] = df["prev_end"] + pd.Timedelta(days=1)
    df.loc[df["end"].isna(), "end"] = df["next_start"] - pd.Timedelta(days=1)
    df.drop(["next_start", "prev_end"], axis=1, inplace=True)
    return df

def fill_quarters(df):
    # Fill the quarter column
    df = df.apply(
        lambda row: fill_quarter(row, df), axis=1
    )
    df["quarter"] = df["quarter"].astype(int)
    return df

def fill_fiscal_years(df, annual_data):
    # Fill the fiscal_year column
    df["fiscal_year"] = df["end"].apply(
        find_fiscal_year, args=(annual_data,)
    )
    return df

def process_quarterly_data(df, annual_data):
    extra_data = df[df["time_delta"] > pd.Timedelta(days=115)]
    df = df.drop(extra_data.index)
    extra_data.reset_index(drop=True, inplace=True)
    df = df.drop_duplicates(subset="value(millions)", keep="last")
    df = df.drop(columns=["time_delta", "filed", "form", "fy", "fp", "accn"])
    df = df.dropna(subset=["frame"])
    df = df.reset_index(drop=True)
    # Merge with the full list of frames
    df_full = generate_full_frames(df)
    df = pd.merge(df_full, df, how="left", on="frame")
    df = df.sort_values(by="frame").reset_index(drop=True)
    # Fill missing start/end dates
    df = fill_dates(df)
    # Remove rows where the 'start' date is on or after the start of the current quarter
    df = remove_future_data(df)
    # Fill missing quarters and fiscal years
    df = fill_quarters(df)
    df = fill_fiscal_years(df, annual_data)
    # Fill missing values for the quarters
    df = fill_missing_quarters(df, annual_data)
    df = df.drop(columns=["frame"])
    df["fiscal_year"] = df["fiscal_year"].astype(int)
    df = df.set_index(["fiscal_year", "quarter"])
    new_merged_order = ["value(millions)", "start", "end"]
    df = df.reindex(columns=new_merged_order)
    return df

def remove_future_data(df):
    # Get the current year and quarter
    current_year = datetime.now().year
    current_month = datetime.now().month
    current_quarter = (current_month - 1) // 3 + 1
    # Get the start date of the current quarter
    start_month = 3 * (current_quarter - 1) + 1
    start_date_current_quarter = datetime(current_year, start_month, 1)
    # Remove rows where the 'start' date is on or after the start of the current quarter
    df = df[df['start'] < start_date_current_quarter]
    return df
   
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

def map_to_quarter(end_date):
    month_diff = (end_date.month - end_month + 9) % 12
    if 0 <= month_diff < 3:
        return 1
    elif 3 <= month_diff < 6:
        return 2
    elif 6 <= month_diff < 9:
        return 3
    else:  # 9, 10, 11
        return 4

def get__concept_data(ticker, concept):
    cik = get_cik(ticker)
    concept_df = get_concept_data(cik, concept)
    annual_data = process_annual_data(concept_df)
    quarterly_data = process_quarterly_data(concept_df, annual_data)
    return annual_data, quarterly_data