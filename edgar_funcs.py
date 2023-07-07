import requests
import pandas as pd

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


def get_10Q_filings_for_ticker(ticker: str) :
    company_filings_df = get_company_filings_for_ticker(ticker)
    ten_Q_df = company_filings_df[company_filings_df["form"] == "10-Q"]
    return ten_Q_df


def get_specific_filing_using_accessionNumber(ticker: str, accessionNumber: str):
    cik = get_cik_for_ticker(ticker)
    headers = {"User-Agent": "russ@sunriseanalysis.com"}
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accessionNumber}"
    req_content = requests.get(url, headers=headers).content.decode("utf-8")
    return req_content


def get_facts_for_ticker(ticker: str) -> pd.DataFrame:
    """
    Get the facts for a given ticker.

    Args:
        ticker (str): The ticker symbol of the company.

    Returns:
        pd.DataFrame: The facts for the company.

    Raises:
        ValueError: If ticker is not a string.
    """
    cik = get_cik_for_ticker(ticker)
    headers = {"User-Agent": "russ@sunriseanalysis.com"}
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{str(cik)}.json"
    company_facts = requests.get(url, headers=headers).json()
    company_facts_df = pd.DataFrame(company_facts["facts"]["us-gaap"])
    return company_facts_df