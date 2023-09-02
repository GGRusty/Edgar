# these are the formulas for the edgar workflow I will detail themn so that it is clear what is happening as well as the idea behind each step all examples will be using the wsm data if there are specifics
import requests
import logging
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from collections import defaultdict

headers = {"User-Agent": "russ@sunriseanalysis.com"}



def get_cik_matching_ticker(ticker: str) -> str:
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
    tickers_json = requests.get(
        "https://www.sec.gov/files/company_tickers.json", headers=headers
    )
    cik_df = pd.DataFrame.from_dict(tickers_json.json(), orient="index")
    cik_df["cik_str"] = cik_df["cik_str"].astype(str).str.zfill(10)
    cik = cik_df[cik_df["ticker"] == ticker]["cik_str"].values[0]
    return cik



def get_submission_data_for_ticker(ticker: str):
    """
    Get the data in json form for a given ticker. For example: 'cik', 'entityType', 'sic', 'sicDescription', 'insiderTransactionForOwnerExists', 'insiderTransactionForIssuerExists', 'name', 'tickers', 'exchanges', 'ein', 'description', 'website', 'investorWebsite', 'category', 'fiscalYearEnd', 'stateOfIncorporation', 'stateOfIncorporationDescription', 'addresses', 'phone', 'flags', 'formerNames', 'filings'

    Args:
        ticker (str): The ticker symbol of the company.

    Returns:
        json: The submissions for the company.

    Raises:
        ValueError: If ticker is not a string.
    """
    cik = get_cik_matching_ticker(ticker)
    headers = {"User-Agent": "russ@sunriseanalysis.com"}
    url = f"https://data.sec.gov/submissions/CIK{str(cik)}.json"
    company_data = requests.get(url, headers=headers).json()
    return company_data




def get_company_filings_df_for_ticker_from_submission_json(ticker: str):
    """
    Get the filings for a given ticker from the submission json.

    Args:
        ticker (str): The ticker symbol of the company.

    Returns:
        pd.DataFrame: The filings for the company.

    Raises:
        ValueError: If ticker is not a string.
    """
    company_data = get_submission_data_for_ticker(ticker)
    company_filings_df = pd.DataFrame(company_data["filings"]["recent"])
    return company_filings_df




def filter_10K_filings_for_ticker(ticker: str) -> pd.DataFrame:
    company_filings_df = get_company_filings_df_for_ticker_from_submission_json(ticker)
    ten_k_df = company_filings_df[company_filings_df["form"] == "10-K"]
    return ten_k_df




def filter_10Q_filings_for_ticker(ticker: str) -> pd.DataFrame:
    company_filings_df = get_company_filings_df_for_ticker_from_submission_json(ticker)
    ten_Q_df = company_filings_df[company_filings_df["form"] == "10-Q"]
    return ten_Q_df 



def get_10K_accessionNumbers_for_ticker(ticker: str) -> pd.Series:
    tenKs = filter_10K_filings_for_ticker(ticker)
    tenKs['reportDate'] = pd.to_datetime(tenKs['reportDate'])
    tenKs.set_index('reportDate', inplace=True)
    tenK_accession_numbers = tenKs['accessionNumber']
    tenK_accession_numbers.name = '10K_accessionNumber'
    tenK_accession_numbers = tenK_accession_numbers.str.replace("-", "")
    return tenK_accession_numbers




def get_10Q_accessionNumbers_for_ticker(ticker: str) -> pd.Series:
    tenQs = filter_10Q_filings_for_ticker(ticker)
    tenQs['reportDate'] = pd.to_datetime(tenQs['reportDate'])
    tenQs.set_index('reportDate', inplace=True)
    tenQ_accession_numbers = tenQs['accessionNumber']
    tenQ_accession_numbers.name = '10Q_accessionNumber'
    tenQ_accession_numbers = tenQ_accession_numbers.str.replace("-", "")
    return tenQ_accession_numbers




def get_facts_for_ticker(ticker: str) -> pd.DataFrame:
    cik = get_cik_matching_ticker(ticker)
    headers = {"User-Agent": "russ@sunriseanalysis.com"}
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{str(cik)}.json"
    company_facts = requests.get(url, headers=headers).json()
    company_facts_df = pd.DataFrame(company_facts["facts"]["us-gaap"])
    return company_facts_df

    


def get_quarterly_facts_for_ticker(ticker: str) -> pd.DataFrame:
    tenQ = filter_10Q_filings_for_ticker(ticker)
    facts = get_explored_facts_for_ticker(ticker)
    quarterly_facts = facts[facts["accn"].isin(tenQ['accessionNumber'])]
    quarterly_facts = quarterly_facts[quarterly_facts['filed'].isin(tenQ['filingDate'])]
    quarterly_facts = quarterly_facts.dropna(subset=['frame'])
    quarterly_pivot = quarterly_facts.pivot_table(index="filed", columns='account_key', values='val').sort_index(ascending=False)
    return quarterly_pivot.T




def get_annual_facts_for_ticker(ticker: str) -> pd.DataFrame:
    tenk_filings = filter_10K_filings_for_ticker(ticker)
    facts = get_explored_facts_for_ticker(ticker)
    annual_facts = facts[facts["accn"].isin(tenk_filings['accessionNumber'])]
    annual_facts = annual_facts[annual_facts['filed'].isin(tenk_filings['filingDate'])]
    annual_facts = annual_facts.dropna(subset=['frame'])
    annual_pivot = annual_facts.pivot_table(index="filed", columns='account_key', values='val').sort_index(ascending=False)
    return annual_pivot.T




def get_specific_filing_using_accessionNumber(ticker: str, accessionNumber: str):
    cik = get_cik_matching_ticker(ticker)
    headers = {"User-Agent": "russ@sunriseanalysis.com"}
    url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accessionNumber}"
    requested_content = requests.get(url, headers=headers).content.decode("utf-8")
    return requested_content 




def get_statement_file_names_in_filing_summary(ticker, accession_number):
    cik = get_cik_matching_ticker(ticker)
    base_link = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession_number}"
    filing_summary_link = f"{base_link}/FilingSummary.xml"
    headers = {"User-Agent": "russ@sunriseanalysis.com"}
    filing_summary_response = requests.get(filing_summary_link, headers=headers)
    soup = BeautifulSoup(filing_summary_response.content, "lxml-xml", from_encoding="utf-8")
    statement_file_names_dict = {}

    for report in soup.find_all("Report"):
        short_name_tag = report.find("ShortName")
        long_name_tag = report.find("LongName")
        html_file_name_tag = report.find("HtmlFileName")
        xml_file_name_tag = report.find("XmlFileName")
        file_name = html_file_name_tag.text if html_file_name_tag else xml_file_name_tag.text if xml_file_name_tag else None

        if long_name_tag and short_name_tag and file_name and "Statement" in long_name_tag.text:
            short_name = short_name_tag.text.lower()
            statement_file_names_dict[short_name] = file_name

    return statement_file_names_dict




def get_statement_soup(ticker, accession_number, statement_name):
    """
    the statement_name should be one of the following:
    
    'balance sheet'
    'income statement'
    'cash flow statement'
    """
    cik = get_cik_matching_ticker(ticker)
    statement_name = statement_name.lower()
    headers = {"User-Agent": "russ@sunriseanalysis.com"}
    base_link = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession_number}"
    statement_file_names_dict = get_statement_file_names_in_filing_summary(ticker, accession_number)
    statement_keys_map = {
        'balance sheet': ['balance sheet', 'consolidated balance sheets'],
        'income statement': ['income statement', 'consolidated statements of operations', 'consolidated statements of earnings'],
        'cash flow statement': ['cash flows statement', 'consolidated statements of cash flows', 'consolidated statements of cash flows (unaudited)']
    }
    
    statement_link = None
    for possible_key in statement_keys_map.get(statement_name, [statement_name]):
        try:
            statement_link = (f"{base_link}/{statement_file_names_dict[possible_key]}")
            break
        except KeyError:
            continue
    
    if statement_link is None:
        raise ValueError(f"Could not find statement with name {statement_name}")
    
    statement_response = requests.get(statement_link, headers=headers)
    if statement_link.endswith(".xml"):
        soup = BeautifulSoup(statement_response.content, "lxml-xml", from_encoding="utf-8")
    else:
        soup = BeautifulSoup(statement_response.content, "lxml")
    
    return soup



def extract_columns_values_and_dates_from_statement(soup: BeautifulSoup):
    columns = []
    values_set = []
    date_time_index = get_datetime_index_dates_from_statement(soup)
    
    for table in soup.find_all("table"):
        unit_multiplier = 1
        table_header = table.find("th")
        if table_header:
            header_text = table_header.get_text()
            if "in Thousands" in header_text:
                unit_multiplier = 1000
            elif "in Millions" in header_text:
                unit_multiplier = 1e6
            if "unless otherwise specified" in header_text:
                special_case = True
        
        for row in table.select("tr"):
            onclick_elements = row.select("td.pl a, td.pl.custom a")
            if not onclick_elements:
                continue
                
            onclick_attr = onclick_elements[0]["onclick"]
            column_title = onclick_attr.split("defref_")[-1].split("',")[0]
            columns.append(column_title)
            
            values = [np.NaN] * len(date_time_index)
            
            for i, cell in enumerate(row.select("td.text, td.nump, td.num")):
                if "text" in cell.get("class"):
                    continue
                
                value = (
                    cell.text.replace("$", "")
                    .replace(",", "")
                    .replace("(", "")
                    .replace(")", "")
                    .strip()
                )
                
                value = keep_numbers_and_decimals_only_in_string(value)
                if value:
                    value = float(value)
                    if not special_case:
                        value *= unit_multiplier
                    else:
                        # Special handling can go here
                        pass
                
                if "nump" in cell.get("class"):
                    values[i] = value / unit_multiplier if unit_multiplier != 1 else value
                else:
                    values[i] = -value / unit_multiplier if unit_multiplier != 1 else -value
            
            values_set.append(values)
    
    return columns, values_set, date_time_index





def get_datetime_index_dates_from_statement(soup: BeautifulSoup) -> pd.DatetimeIndex:
    """
    Extract both index dates from the HTML soup object.
    stores them in a list
    """
    table_headers = soup.find_all("th", {'class': 'th'})
    dates = [str(th.div.string) for th in table_headers if th.div and th.div.string]
    index_dates = pd.to_datetime(dates)
    return index_dates




def create_dataframe_of_statement_values_columns_dates(values_set, columns, index_dates) -> pd.DataFrame:
    """
    Modified to create DataFrame with two rows.
    """
    transposed_values_set = list(zip(*values_set))
    df = pd.DataFrame(transposed_values_set, columns=columns, index=index_dates)
    return df




def process_one_statement(ticker, accession_number, statement_name):
    try:
        soup = get_statement_soup(ticker, accession_number, statement_name)
    except Exception as e:
        logging.error(
            f"Failed to get statement soup: {e} for accession number: {accession_number}"
        )
        soup = None
    if soup is not None:
        columns, values, dates = extract_columns_values_and_dates_from_statement(soup)
        df = create_dataframe_of_statement_values_columns_dates(values, columns, dates)
        df = df.loc[:, ~df.columns.duplicated()]
        if df.empty:
            logging.warning(f"Empty DataFrame for accession number: {accession_number}")
            pass
        else:
            return df
 
      


def form_statement_for_all_available_years(ticker, statement_name):
    accession_number_series = get_10K_accessionNumbers_for_ticker(ticker)
    all_available_years = pd.DataFrame()
    for accession_number in accession_number_series:
        df = process_one_statement(ticker, accession_number, statement_name)
        all_available_years = pd.concat([all_available_years, df], axis=0, join="outer")
        print(
            f"{statement_name} for accession number: {accession_number} has been processed."
        )
        df_combined = (
            all_available_years.groupby(all_available_years.index)
            .agg(custom_aggregator)
            .sort_index(ascending=False)
        )
    return df_combined.T
    



"""

Helper functions for the main functions below

"""

def custom_aggregator(series):
    first_val = series.iloc[0]
    for value in series[1:]:
        if pd.isna(first_val) and not pd.isna(value):
            first_val = value 
    return first_val


def retrieve_balance_income_cf_and_store_as_CSV(ticker, blank: bool = True):
    earnings_sheet = form_statement_for_all_available_years(ticker, "consolidated statements of earnings")
    balance_sheet = form_statement_for_all_available_years(ticker, "consolidated balance sheets")
    cash_flow_sheet = form_statement_for_all_available_years(ticker, "consolidated statements of cash flows")
    all_three_statements = pd.concat(
    [balance_sheet, earnings_sheet, cash_flow_sheet],
    keys=["balance_sheet", "earnings_sheet", "cash_flow_sheet"],
)
    if blank == True:
        all_three_statements = all_three_statements.replace(["None", np.NaN], "")
    save_dataframe_to_csv(cash_flow_sheet, ticker, "consolidated statements of cash flows", "annual")
    save_dataframe_to_csv(balance_sheet, ticker, "consolidated balance sheets", "annual")
    save_dataframe_to_csv(earnings_sheet, ticker, "consolidated statements of earnings", "annual")
    save_dataframe_to_csv(all_three_statements, ticker, "all_three_main_statements", "annual")
    return all_three_statements
 
    
def save_dataframe_to_csv(dataframe, ticker, statement_name, frequency):
    dataframe.to_csv(f"results/{ticker}/{statement_name}_{frequency}.csv")
    return None
    
    
def print_links_to_desired_statment(ticker, statement_name):
    statement_name = statement_name.lower()
    acc_series = get_10K_accessionNumbers_for_ticker(ticker)
    cik = get_cik_matching_ticker(ticker)
    for accession_number in acc_series:
        base_link = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession_number}"
        try:
            statement_file_names_dict = get_statement_file_names_in_filing_summary(ticker, accession_number)
            statement_link = f"{base_link}/{statement_file_names_dict[statement_name]}"
        except:
            continue
        print(statement_link)
    return None
    
    
def keep_numbers_only_in_string(mixed_string: str):
    return "".join([character for character in mixed_string if character.isdigit()])


def keep_numbers_and_decimals_only_in_string(mixed_string: str):
    num = "1234567890."
    allowed = list(filter(lambda x: x in num, mixed_string))
    return "".join(allowed)


def keep_letters_and_numbers_only_in_string(mixed_string: str):
    alpha_num = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
    allowed = list(filter(lambda x: x in alpha_num, mixed_string))
    return "".join(allowed)


def check_units_in_thousands_or_millions(soup: BeautifulSoup) -> (bool, bool):
    content = soup.text.lower()
    in_thousands = "in thousands" in content
    in_millions = "in millions" in content
    return in_thousands, in_millions


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


def get_explored_facts_for_ticker(ticker: str) -> pd.DataFrame:
    facts = get_facts_for_ticker(ticker).T
    facts = facts["units"]
    facts_dict = facts.to_dict()
    facts = explore_facts_dict(facts_dict)
    return facts




"""

functions that do not work yet but are in progress

"""




def create_many_to_one_name_mapping_to_statement(soup: BeautifulSoup) -> dict:
    """
    Modified to create a many-to-one dictionary. still need to implement
    """
    column_name_mapping = defaultdict(list)
    for row in soup.select("tr.re, tr.ro, tr.reu, tr.rou"):
        onclick_attr = row.select_one("td.pl a, td.pl.custom a")["onclick"]
        column_title = onclick_attr.split("defref_")[-1].split("',")[0]
        displayed_name = row.select_one("td.pl a, td.pl.custom a").text.strip()
        displayed_name = keep_letters_and_numbers_only_in_string(displayed_name).lower()
        column_name_mapping[displayed_name].append(column_title)
    return column_name_mapping




def rename_df_columns_using_mapping(
    df: pd.DataFrame, column_name_mapping: dict
) -> pd.DataFrame:
    """
    Rename columns in the DataFrame using the many-to-one mapping dictionary.

    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - column_name_mapping (dict): The many-to-one mapping dictionary.

    Returns:
    - pd.DataFrame: DataFrame with renamed columns.
    """
    # Create a reverse mapping from internal column title to displayed name
    reverse_mapping = {
        col: disp_name
        for disp_name, cols in column_name_mapping.items()
        for col in cols
    }
    # Rename columns in the DataFrame
    df = df.rename(columns=reverse_mapping)

    return df




def create_column_name_mapping_to_statement(soup: BeautifulSoup) -> dict:
    """
    Create a dictionary that maps internal column titles to displayed names.
    
    Parameters:
    - soup (BeautifulSoup): The HTML soup object containing the balance sheet.
    
    Returns:
    - dict: Dictionary mapping internal column titles to displayed names.
    """
    column_name_mapping = {}
    
    # Iterate through each row in the balance sheet table
    for row in soup.select("tr.re, tr.ro, tr.reu, tr.rou"):
        
        # Extract the 'onclick' attribute to get the internal column title
        onclick_attr = row.select_one("td.pl a, td.pl.custom a")["onclick"]
        column_title = onclick_attr.split("defref_")[-1].split("',")[0]
        
        # Extract the displayed name from the table cell
        displayed_name = row.select_one("td.pl a, td.pl.custom a").text.strip()
        displayed_name = keep_letters_and_numbers_only_in_string(displayed_name)
        # Add to the dictionary
        column_name_mapping[column_title] = displayed_name
    
    return column_name_mapping