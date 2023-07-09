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


def get_parsed_facts(ticker) -> pd.DataFrame:
    cik = get_cik_for_ticker(ticker)
    headers = {"User-Agent": "russ@sunriseanalysis.com"}
    tenKs = get_10K_accessionNumbers_for_ticker(ticker)
    tenQs = get_10Q_accessionNumbers_for_ticker(ticker)
    combinced_10Ks_10Qs = pd.concat([tenKs, tenQs], join='outer')
    facts = get_facts_for_ticker(ticker).T
    facts.index.name = 'fact'
    facts = facts['units']
    facts_dict = facts.to_dict()
    facts_df = explore_facts_dict(facts_dict)
    facts_df = facts_df[facts_df['accn'].isin(combinced_10Ks_10Qs)].dropna(subset=['frame'])
    facts_df = facts_df.drop(['accn', 'start', 'fy', 'fp', 'frame', 'filed', 'form'], axis=1)
    facts_df['fact__unit'] = facts_df['account_key'] + '__' + facts_df['unit_key']
    facts_df = facts_df.drop(['account_key', 'unit_key'], axis=1)
    pivot_df = facts_df.pivot_table(index='end', columns='fact__unit', values='val', aggfunc='first')
    pivot_df.index = pd.to_datetime(pivot_df.index)
    pivot_df_recent= pivot_df[pivot_df.index.isin(combinced_10Ks_10Qs.index)]
    pivot_df_recent = pivot_df_recent.dropna(axis=1, how='all')
    for col in pivot_df_recent.columns:
        if '_USD' in col or '_shares' in col and pivot_df_recent[col].abs().max() > 1_000:
            pivot_df_recent[col] = pivot_df_recent[col] / 1_000_000
            pivot_df_recent.rename(columns={col: col + '(millions)'}, inplace=True)
    pivot_df_recent.name = ticker
    return pivot_df_recent

def get_parsed_facts_in_csv(ticker) -> None:
    if not os.path.exists('facts_data'):
        os.makedirs('facts_data')
    parsed_facts_df = get_parsed_facts(ticker)
    parsed_facts_df.to_csv(f'facts_data/{ticker}_parsed_edgar_facts.csv')