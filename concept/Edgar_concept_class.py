import requests
import pandas as pd
import numpy as np
import datetime

class EdgarConcept:
    """
    This class fetches and processes financial concept data from the EDGAR database for a given company.

    Args:
        ticker (str): The ticker symbol of the company.
        concept (str): The financial concept to fetch data for.
        headers (dict): Request headers to use when fetching data.

    Attributes:
        ticker (str): The ticker symbol of the company.
        concept (str): The financial concept to fetch data for.
        headers (dict): Request headers to use when fetching data.
        concept_df (DataFrame): Raw concept data fetched from the EDGAR database.
        unit_df (DataFrame): Unit data extracted from the concept data.
        annual_data (DataFrame): Processed annual data.
        quarterly_data (DataFrame): Processed quarterly data.    
            
    """
    def __init__(self, ticker: str, concept: str, headers: dict):
        """
        Initialize a new EdgarConcept object.

        Args:
            ticker (str): The ticker symbol of the company.
            concept (str): The financial concept to fetch data for.
            headers (dict): Request headers to use when fetching data.

        Raises:
            ValueError: If ticker or concept is not a string.
            ValueError: If headers is not a dict.
        """
        self.ticker = ticker
        self.concept = concept
        self.headers = headers
        self.concept_df = self.get_concept_data()
        self.unit_df = self.get_unit_data()
        self.annual_data, self.quarterly_data = self.process_data()

    @staticmethod
    def get_cik(ticker: str) -> str:
        """
        Get the CIK for a given ticker.

        Args:
            ticker (str): The ticker symbol of the company.

        Returns:
            str: The CIK for the company.

        Raises:
            ValueError: If ticker is not a string.
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

    def get_concept_data(self) -> pd.DataFrame:
        """
        Fetch concept data from the EDGAR database for the current object.

        Returns:
            DataFrame: The concept data.

        Raises:
            Exception: If an error occurs while fetching the concept data.
        """
        cik = self.get_cik(self.ticker)
        concept_url = f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/us-gaap/{self.concept}.json"
        concept_df = pd.DataFrame.from_dict(requests.get(concept_url, headers=self.headers).json())
        return concept_df

    def get_unit_data(self) -> pd.DataFrame:
        """
        Process the concept data to extract the unit data.

        Returns:
            DataFrame: The unit data, with the following columns:

            start: The start date of the period.
            end: The end date of the period.
            filed: The date the filing was made.
            time_delta: The difference between the end and start dates.
            value(millions): The value of the unit, in millions.
        """
        df = pd.DataFrame.from_dict(self.concept_df["units"]["USD"])
        for col in ["start", "end", "filed"]:
            df[col] = pd.to_datetime(df[col])
        df["time_delta"] = df["end"] - df["start"]
        df["val"] = df["val"] / 1_000_000
        df.rename(columns={"val": "value(millions)"}, inplace=True)
        return df

    @staticmethod
    def map_to_quarter(end_date, end_month: int) -> int:
        """
        Converts a date to the corresponding financial quarter.

        Args:
            end_date (datetime): The date to convert.
            end_month (int): The end month of the quarter.

        Returns:
            int: The corresponding financial quarter.

        Raises:
            ValueError: If end_date is not a datetime object.
            ValueError: If end_month is not an integer.
        """
        month_diff = (end_date.month - end_month + 9) % 12
        if 0 <= month_diff < 3:
            return 1
        elif 3 <= month_diff < 6:
            return 2
        elif 6 <= month_diff < 9:
            return 3
        else:  # 9, 10, 11
            return 4
       
    def fill_quarter(self, row, quarterly_data):
        """
        Fills in missing quarters for the provided row.

        Args:
            row (pd.Series): The row to fill in.
            quarterly_data (pd.DataFrame): The DataFrame with the quarterly data.

        Returns:
            pd.Series: The row with missing quarters filled in.
        """
        if pd.isnull(row["quarter"]):
            previous_index = row.name - 1
            next_index = row.name + 1 if row.name < len(quarterly_data) - 1 else row.name
            if previous_index >= 0 and not pd.isnull(quarterly_data.loc[previous_index, "quarter"]):
                previous_quarter = quarterly_data.loc[previous_index, "quarter"]
                row["quarter"] = 1 if previous_quarter == 4 else previous_quarter + 1
            elif not pd.isnull(quarterly_data.loc[next_index, "quarter"]):
                next_quarter = quarterly_data.loc[next_index, "quarter"]
                row["quarter"] = 4 if next_quarter == 1 else next_quarter - 1
        return row

    def find_fiscal_year(self, date, annual_data):
        """
        Finds the fiscal year for the provided date and annual DataFrame.

        Args:
            date (datetime): The date to find the fiscal year for.
            annual_data (pd.DataFrame): The annual DataFrame with the fiscal year information.

        Returns:
            str: The fiscal year.

        Raises:
            ValueError: If date is not a datetime object.
            ValueError: If annual_data is not a pandas DataFrame.
        """
        for idx, row in annual_data.iterrows():
            if row["start"] <= date <= row["end"]:
                return row["fiscal_year"]
        last_fiscal_year_end = annual_data["end"].max()
        if date > last_fiscal_year_end:
            last_year = int(annual_data.iloc[-1]["fiscal_year"][2:])
            next_year = last_year + 1
            return "CY" + str(next_year)
        return None
    
    def fill_missing_quarters(self, quarterly_data, annual_data):
        """
        Fills in missing quarters for the provided DataFrame.

        Args:
            quarterly_data (pd.DataFrame): The DataFrame to fill in.
            annual_data (pd.DataFrame): The annual DataFrame with the full year values.

        Returns:
            pd.DataFrame: The DataFrame with missing quarters filled in.

        Raises:
            ValueError: If quarterly_data or annual_data is not a pandas DataFrame.
        """
        for idx, row in quarterly_data.iterrows():
            if pd.isnull(row["value(millions)"]):
                other_quarters = quarterly_data[
                    (quarterly_data["fiscal_year"] == row["fiscal_year"]) & (quarterly_data.index != idx)
                ]["value(millions)"]
                if other_quarters.count() == 3:
                    annual_value = annual_data[
                        annual_data["fiscal_year"] == row["fiscal_year"]
                    ]["value(millions)"].values[0]
                    sum_of_quarters = other_quarters.sum()
                    quarterly_data.at[idx, "value(millions)"] = annual_value - sum_of_quarters
        return quarterly_data
    
    def process_data(self):
        """
        Processes the fetched concept data to extract annual and quarterly data.

        Returns:
            tuple: The annual and quarterly data as two separate DataFrames.

        """
        # get the unit data
        df = self.unit_df
        # extract the annual data
        annual_data = df[df["time_delta"] > pd.Timedelta(days=350)]
        # drop the annual data from the unit data
        df = df.drop(annual_data.index)
        # remove duplicates
        annual_data = annual_data.drop_duplicates(subset="value(millions)", keep="last")
        annual_data = annual_data.dropna(subset="frame")
        annual_data = annual_data.drop(
            columns=["time_delta", "filed", "form", "fy", "fp"]
        ).reset_index(drop=True)
        annual_data.rename(columns={"frame": "fiscal_year"}, inplace=True)
        # extraacts the extra data
        extra_data = df[df["time_delta"] > pd.Timedelta(days=115)]
        df = df.drop(extra_data.index)
        extra_data.reset_index(drop=True, inplace=True)
        df = df.drop_duplicates(subset="value(millions)", keep="last")
        df = df.drop(columns=["time_delta", "filed", "form", "fy", "fp", "accn"])
        df = df.dropna(subset=["frame"])
        df = df.reset_index(drop=True)
        # this gets the end month of the first annual period
        end_month = annual_data.iloc[0]["end"].month
        # this maps the end month to the quarter that it belongs to
        df["quarter"] = df["end"].apply(lambda x: self.map_to_quarter(x, end_month))
        start_year = int(df["frame"].min()[2:6])  # extract start year from the minimum frame
        end_year = int(df["frame"].max()[2:6])  # extract end year from the maximum frame
        # create a list of all the frames for the quarterly data
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
        quarterly_data.loc[quarterly_data["end"].isna(), "end"] = quarterly_data["next_start"] - pd.Timedelta(days=1) # type: ignore
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
        quarterly_data = quarterly_data.apply(lambda row: self.fill_quarter(row, quarterly_data), axis=1)
        quarterly_data["quarter"] = quarterly_data["quarter"].astype(int)
        # Apply the function to the 'end' column in 'df'
        quarterly_data["fiscal_year"] = quarterly_data["end"].apply(self.find_fiscal_year, args=(annual_data,))
        # Apply the function to the DataFrame
        quarterly_data = self.fill_missing_quarters(quarterly_data, annual_data)
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

    def get_data_point(self, year: int, quarter: int) -> pd.Series:
        """
        Gets the data point for the specified year and quarter.

        Args:
            year (int): The year of the data point.
            quarter (int): The quarter of the data point.

        Returns:
            pd.Series: The data point for the specified year and quarter.

        Raises:
            KeyError: If the specified year and quarter are not found in the quarterly data.
        """
        if quarter < 1 or quarter > 4:
            raise ValueError("quarter must be between 1 and 4")
        return self.quarterly_data.loc[(year, quarter)]
