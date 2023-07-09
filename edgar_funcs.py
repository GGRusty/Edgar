import os
import requests
import pandas as pd

headers = {"User-Agent": "russ@sunriseanalysis.com"}

def get_cik_for_ticker(ticker: str) -> str:
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


def get_ciks_matching_tickers_df():
    headers = {"User-Agent": "russ@sunriseanalysis.com"}
    # Get the tickers JSON file
    tickers_json = requests.get(
        "https://www.sec.gov/files/company_tickers.json", headers=headers
    )
    # Create a DataFrame of the tickers
    cik_df = pd.DataFrame.from_dict(tickers_json.json(), orient="index")
    return cik_df


def get_companies_names_containing_string(string: str) -> pd.DataFrame:
    cik_df = get_ciks_matching_tickers_df()
    substring = string 
    contains_substring = cik_df[cik_df['title'].str.contains(substring, case=False)]
    return contains_substring


def get_company_data_for_ticker(ticker: str):
    """
    Get the data in json form for a given ticker. For example: 'cik', 'entityType', 'sic', 'sicDescription', 'insiderTransactionForOwnerExists', 'insiderTransactionForIssuerExists', 'name', 'tickers', 'exchanges', 'ein', 'description', 'website', 'investorWebsite', 'category', 'fiscalYearEnd', 'stateOfIncorporation', 'stateOfIncorporationDescription', 'addresses', 'phone', 'flags', 'formerNames', 'filings'

    Args:
        ticker (str): The ticker symbol of the company.

    Returns:
        pd.DataFrame: The submissions for the company.

    Raises:
        ValueError: If ticker is not a string.
    """
    cik = get_cik_for_ticker(ticker)
    headers = {"User-Agent": "russ@sunriseanalysis.com"}
    url = f"https://data.sec.gov/submissions/CIK{str(cik)}.json"
    company_data = requests.get(url, headers=headers).json()
    return company_data


def get_company_filings_for_ticker(ticker: str):
    """
    Get the filings for a given ticker.

    Args:
        ticker (str): The ticker symbol of the company.

    Returns:
        pd.DataFrame: The filings for the company.

    Raises:
        ValueError: If ticker is not a string.
    """
    company_data = get_company_data_for_ticker(ticker)
    company_filings_df = pd.DataFrame(company_data["filings"]["recent"])
    return company_filings_df

    
def get_10K_filings_for_ticker(ticker: str) -> pd.DataFrame:
    company_filings_df = get_company_filings_for_ticker(ticker)
    ten_k_df = company_filings_df[company_filings_df["form"] == "10-K"]
    return ten_k_df


def get_10K_accessionNumbers_for_ticker(ticker: str) -> pd.Series:
    tenKs = get_10K_filings_for_ticker(ticker)
    tenKs['reportDate'] = pd.to_datetime(tenKs['reportDate'])
    tenKs.set_index('reportDate', inplace=True)
    tenK_accession_numbers = tenKs['accessionNumber']
    tenK_accession_numbers.name = '10K_accessionNumber'
    return tenK_accession_numbers


def get_10Q_filings_for_ticker(ticker: str) -> pd.DataFrame:
    company_filings_df = get_company_filings_for_ticker(ticker)
    ten_Q_df = company_filings_df[company_filings_df["form"] == "10-Q"]
    return ten_Q_df


def get_10Q_accessionNumbers_for_ticker(ticker: str) -> pd.Series:
    tenQs = get_10Q_filings_for_ticker(ticker)
    tenQs['reportDate'] = pd.to_datetime(tenQs['reportDate'])
    tenQs.set_index('reportDate', inplace=True)
    tenQ_accession_numbers = tenQs['accessionNumber']
    tenQ_accession_numbers.name = '10Q_accessionNumber'
    return tenQ_accession_numbers


def get_quarterly_and_annual_accn_series(ticker: str):  # this is goint to replace the two get 10k and 10q accession number functions above
    """Gets a series of the accession numbers for the most recent 10-Q and 10-K filings
    for the 4th quarter of the quarterly series we added the 10-K accession numbers
    returns two series, one for the 10-Q and one for the 10-K"""
    recent_df = get_company_filings_for_ticker(ticker)
    # Convert 'recent' data to a DataFrame
    filings_10Q = recent_df[recent_df['form'] == '10-Q']
    filings_10K = recent_df[recent_df['form'] == '10-K']

    # Create Series with report date as index and accession number as values
    series_10Q = filings_10Q.set_index('reportDate')['accessionNumber']
    series_10K = filings_10K.set_index('reportDate')['accessionNumber']

    # For the quarterly series, add the annual one where the dates are missing
    series_10Q = series_10Q.combine_first(series_10K)
    return series_10Q, series_10K


def get_specific_filing_using_accessionNumber(ticker: str, accessionNumber: str):
    cik = get_cik_for_ticker(ticker)
    headers = {"User-Agent": "russ@sunriseanalysis.com"}
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accessionNumber}"
    req_content = requests.get(url, headers=headers).content.decode("utf-8")
    return req_content


def get_facts_for_ticker(ticker: str) -> pd.DataFrame:
    cik = get_cik_for_ticker(ticker)
    headers = {"User-Agent": "russ@sunriseanalysis.com"}
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{str(cik)}.json"
    company_facts = requests.get(url, headers=headers).json()
    company_facts_df = pd.DataFrame(company_facts["facts"]["us-gaap"])
    return company_facts_df


def explore_facts_dict(data) -> pd.DataFrame:
    rows = []
    for account_key, account_values in data.items():
        for unit_key, unit_values in account_values.items():
            for item in unit_values:
                row = {"account_key": account_key, "unit_key": unit_key}
                row.update(item)
                rows.append(row)
    df = pd.DataFrame(rows)
    return df


def split_and_process_facts(ticker: str):
    tenQs, tenKs = get_quarterly_and_annual_accn_series(ticker)
    facts = get_facts_for_ticker(ticker).T
    facts.index.name = "fact"
    facts = facts["units"]
    facts_dict = facts.to_dict()
    facts_df = explore_facts_dict(facts_dict)
    annual_df = facts_df[facts_df["accn"].isin(tenKs)]
    quarterly_df = facts_df[facts_df["accn"].isin(tenQs)].dropna(subset=["frame"])
    annual_df = annual_df.drop(["accn", "start", "fy", "fp", "frame", "filed", "form"], axis=1)
    quarterly_df = quarterly_df.drop(["accn", "start", "fy", "fp", "frame", "filed", "form"], axis=1)
    annual_df["fact__unit"] = annual_df["account_key"] + "__" + annual_df["unit_key"]
    quarterly_df["fact__unit"] = (quarterly_df["account_key"] + "__" + quarterly_df["unit_key"])
    annual_df = annual_df.drop(["account_key", "unit_key"], axis=1)
    quarterly_df = quarterly_df.drop(["account_key", "unit_key"], axis=1)
    annual_pivot = annual_df.pivot_table(index="end", columns="fact__unit", values="val", aggfunc="first")
    quarterly_pivot = quarterly_df.pivot_table(index="end", columns="fact__unit", values="val", aggfunc="first")
    annual_pivot.index = pd.to_datetime(annual_pivot.index)
    quarterly_pivot.index = pd.to_datetime(quarterly_pivot.index)
    annual_recent = annual_pivot[annual_pivot.index.isin(tenKs.index)]
    quarterly_recent = quarterly_pivot[quarterly_pivot.index.isin(tenQs.index)]
    annual_recent = annual_recent.dropna(axis=1, how="all")
    quarterly_recent = quarterly_recent.dropna(axis=1, how="all")
    annual_recent.name = "annual_DataFrame"
    quarterly_recent.name = "quarterly_DataFrame"
    ## the code below kinda complicates things, so I'm commenting it out for now its a little ahead of its time
    ## it divides the dataframe by 1000000 but i can worry about readability after it works
    # for col in annual_recent.columns:
    #     if "_USD" in col or "_shares" in col and annual_recent[col].abs().max() > 1_000:
    #         annual_recent[col] = annual_recent[col] / 1_000_000
    #         annual_recent.rename(columns={col: col + "(millions)"}, inplace=True)
    # for col in quarterly_recent.columns:
    #     if "_USD" in col or "_shares" in col and quarterly_recent[col].abs().max() > 1_000:
    #         quarterly_recent[col] = quarterly_recent[col] / 1_000_000
    #         quarterly_recent.rename(columns={col: col + "(millions)"}, inplace=True)
    return quarterly_recent, annual_recent

def get_parsed_facts_in_csv(ticker: str) -> None:
    if not os.path.exists(f'{ticker}_facts_data'):
        os.makedirs(f'{ticker}_facts_data')
    quarterly, annual = split_and_process_facts(ticker)
    quarterly.to_csv(f'{ticker}_facts_data/{ticker}_quarterly_edgar_facts.csv')
    annual.to_csv(f'{ticker}_facts_data/{ticker}_annual_edgar_facts.csv')
    return print(f'CSV files for {ticker} have been created in the {ticker}_facts_data folder')
