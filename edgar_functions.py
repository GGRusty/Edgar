import os
import requests
import logging
import calendar
import numpy as np
import pandas as pd
from lxml import etree
from bs4 import BeautifulSoup

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
    ticker = ticker.replace(".", "-")
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




def filter_accession_number_index_page(df, column_name, search_term):
    fitered_df = df[df[column_name].str.contains(search_term, case=False, na=False)]
    filtered_list = fitered_df[column_name].tolist()
    return filtered_list




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
    'balance_sheet'
    'income_statement'
    'cash_flow_statement'
    """
    cik = get_cik_matching_ticker(ticker)
    statement_name = statement_name.lower()
    headers = {"User-Agent": "russ@sunriseanalysis.com"}
    base_link = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession_number}"
    statement_file_names_dict = get_statement_file_names_in_filing_summary(ticker, accession_number)
    statement_keys_map = {
        'balance_sheet': [
            'balance sheet',
            'balance sheets',
            'statement of financial position',
            'consolidated balance sheets',
            'consolidated balance sheet',
            'consolidated financial position',
            'consolidated balance sheets - southern',
            'consolidated statements of financial position',
            'consolidated statement of financial position',
            'consolidated statements of financial condition',
            'combined and consolidated balance sheet',
            'condensed consolidated balance sheets',
            'consolidated balance sheets, as of december 31',
            'dow consolidated balance sheets',
            'consolidated balance sheets (unaudited)',
        ],
        'income_statement': [
            'income statement',
            'income statements',
            'statement of earnings (loss)',
            'statements of consolidated income',
            'consolidated statements of operations',
            'consolidated statement of operations', 
            'consolidated statements of earnings', 
            'consolidated statement of earnings',
            'consolidated statements of income', 
            'consolidated statement of income',
            'consolidated income statements',
            'consolidated income statement',
            'condensed consolidated statements of earnings',
            'consolidated results of operations',
            'consolidated statements of income (loss)',
            'consolidated statements of income - southern',
            'consolidated statements of operations and comprehensive income',
            'consolidated statements of comprehensive income',
        ],
        'cash_flow_statement': [
            'cash flows statement',
            'cash flows statements',
            'statement of cash flows',
            'statements of consolidated cash flows',
            'consolidated statements of cash flows',
            'consolidated statement of cash flows',
            'consolidated statement of cash flow',
            'consolidated cash flows statements',
            'consolidated cash flow statements',
            'condensed consolidated statements of cash flows',
            'consolidated statements of cash flows (unaudited)',
            'consolidated statements of cash flows - southern',
        ]
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




def get_label_dictionary(ticker, accession_number):
    cik = get_cik_matching_ticker(ticker)
    headers = {"User-Agent": "russ@sunriseanalysis.com"}
    base_url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession_number}"
    requested_content = requests.get(base_url, headers=headers).content.decode("utf-8")
    filing = pd.read_html(requested_content)
    try:
        label_link = filter_accession_number_index_page(filing[0], "Name", "_lab.xml")
    except:
        return None
    label_link = f"{base_url}/{label_link[0]}"
    label_content = requests.get(label_link, headers=headers).content
    tree_lab = etree.fromstring(label_content, parser=etree.XMLParser(recover=True))
    namespaces = tree_lab.nsmap
    label_dictionary = {}
    for label in tree_lab.xpath("//link:label", namespaces=namespaces):
        gaap_fact = label.get("{http://www.w3.org/1999/xlink}label", None).split(
            "_", 1
        )[-1]
        human_readable_label = label.text
        label_dictionary[gaap_fact] = human_readable_label
    return label_dictionary




def extract_columns_values_and_dates_from_statement(soup: BeautifulSoup):
    columns = []
    values_set = []
    date_time_index = get_datetime_index_dates_from_statement(soup)
    special_case = False
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
                    .strip())
                value = keep_numbers_and_decimals_only_in_string(value)
                if value:
                    value = float(value)
                    if not special_case:
                        value *= unit_multiplier
                    else:
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
    dates = [standardize_date(date).replace('.','') for date in dates]
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
    



def form_statement_for_all_available_quarters(ticker, statement_name):
    accession_number_series = get_10Q_accessionNumbers_for_ticker(ticker)
    all_available_quarters = pd.DataFrame()
    for accession_number in accession_number_series:
        df = process_one_statement(ticker, accession_number, statement_name)
        all_available_quarters = pd.concat([all_available_quarters, df], axis=0, join="outer")
        print(
            f"{statement_name} for accession number: {accession_number} has been processed."
        )
        df_combined = (
            all_available_quarters.groupby(all_available_quarters.index)
            .agg(custom_aggregator)
            .sort_index(ascending=False)
        )
    return df_combined.T




def rename_statement(statement, label_dictionary):
    statement.index = statement.index.map(lambda x: label_dictionary.get(x, x))
    return statement




def create_simple_statement(statement, mapping):
    statement = statement.T
    new_statement = pd.DataFrame(index=statement.index, columns=mapping.keys())
    for common_name, gaap_names in mapping.items():
        for gaap_name in gaap_names:
            if gaap_name in statement.columns:
                if new_statement[common_name].isnull().all():
                    new_statement[common_name] = statement[gaap_name]
                else:
                    new_statement[common_name].fillna(statement[gaap_name], inplace=True)
    
    return new_statement




def create_scorecard_from_simple_statements(income_sheet, balance_sheet, cash_flow_sheet):
    scorecard = pd.DataFrame()
    scorecard['Net Revenue'] = income_sheet['Net Revenue']
    scorecard['COGS'] = income_sheet['Cost of Goods Sold']
    scorecard['Gross Profit'] = income_sheet['Gross Profit']
    scorecard['SG&A'] = income_sheet['SG&A']
    scorecard['Operating Expenses'] = income_sheet['SG&A']
    scorecard['Operating Income'] = income_sheet['Operating Income']
    scorecard['Interest Expense'] = income_sheet['Interest Expense']
    scorecard['EBT'] = income_sheet['EBT']
    scorecard['Taxes'] = income_sheet['Taxes']
    scorecard['Tax Rate'] = scorecard['Taxes'] / scorecard['EBT']
    scorecard['Net Income'] = income_sheet['Net income']
    scorecard['EPS'] = income_sheet['EPS']
    scorecard['EPS Diluted'] = income_sheet['EPS Diluted']
    scorecard['EBITDA'] = income_sheet['EBT'] + income_sheet['Interest Expense'] + cash_flow_sheet['Depreciation and Amortization']
    scorecard['Dividend per Share(diluted)'] = (-cash_flow_sheet['Payment of Dividends']) / income_sheet['Weighted Average Shares Diluted']
    scorecard['Dividend Payout Ratio'] = scorecard['Dividend per Share(diluted)'] / scorecard['EPS Diluted']
    scorecard['Cash'] = balance_sheet['Cash']
    scorecard['Accounts Receivable'] = balance_sheet['Accounts Receivable']
    scorecard['Inventory'] = balance_sheet['Inventory']
    scorecard['Other Current Assets'] = balance_sheet['Other Current Assets']
    scorecard['Total Current Assets'] = balance_sheet['Total Current Assets']
    scorecard['Property, Plant & Equipment, Net'] = balance_sheet['Property, Plant, and Equipment']
    scorecard['Goodwill'] = balance_sheet['Goodwill']
    scorecard['Total Assets'] = balance_sheet['Total Assets']
    scorecard['Accrued Expenses'] = balance_sheet['Accrued Expenses']
    scorecard['Deferred Revenue'] = balance_sheet['Deferred Revenue']
    scorecard['Income Tax Payable'] = balance_sheet['Income Taxes Payable']
    scorecard['Operating Lease Liability'] = balance_sheet['Operating Lease Liability']
    scorecard['Other Current Liabilities'] = balance_sheet['Other Current Liabilities']
    scorecard['Accounts Payable'] = balance_sheet['Accounts Payable']
    scorecard['Total Current Liabilities'] = balance_sheet['Total Current Liabilities']
    scorecard['Deffered Lease Incentives'] = balance_sheet['Deffered Lease Incentive']
    scorecard['Long Term Lease Liability'] = balance_sheet['Long Term Lease Liability']
    scorecard['Other Long Term Liabilities'] = balance_sheet['Other Long Term Liabilities']
    scorecard['Total Liabilities'] = balance_sheet['Total Liabilities']
    scorecard['Equity'] = balance_sheet['Total Stockholders Equity']
    scorecard['Total Liabilities and Equity'] = balance_sheet['Total Liabilities and Stockholders Equity']
    scorecard['Book Value per Share'] = balance_sheet['Total Stockholders Equity'] / income_sheet['Weighted Average Shares Diluted']
    scorecard['Operating Cash Flow'] = cash_flow_sheet['Net Cash Provided by Operating Activities']
    scorecard['OCF/NI'] = scorecard['Operating Cash Flow'] / scorecard['Net Income']
    scorecard['Depreciation & Amortization'] = cash_flow_sheet['Depreciation and Amortization']
    scorecard['Capital Expenditure'] = -cash_flow_sheet['Purchase of Property, Plant, and Equipment']
    scorecard['Free Cash Flow'] = scorecard['Operating Cash Flow'] + scorecard['Capital Expenditure']
    scorecard['Capex/Depreciation'] = scorecard['Capital Expenditure'] / scorecard['Depreciation & Amortization']
    scorecard['Dividends'] = -cash_flow_sheet['Payment of Dividends']
    scorecard['Stock Repurchase'] = -cash_flow_sheet['Repurchases of Common Stock']
    scorecard['ROA'] = scorecard['Net Income'] / scorecard['Total Assets']
    scorecard['ROE'] = scorecard['Net Income'] / scorecard['Equity']
    scorecard['Profit Margin'] = scorecard['Net Income'] / scorecard['Net Revenue']
    scorecard['Asset Turnover'] = scorecard['Net Revenue'] / scorecard['Total Assets']
    scorecard['Current Ratio'] = scorecard['Total Current Assets'] / scorecard['Total Current Liabilities']
    scorecard['Equity Multiplier'] = scorecard['Total Assets'] / scorecard['Equity']
    scorecard['Net Working Capital'] = scorecard['Total Current Assets'] - scorecard['Total Current Liabilities']
    scorecard['Debt to Equity Ratio'] = scorecard['Total Liabilities'] / scorecard['Equity']
    scorecard['Days of Sales Outstanding'] = (scorecard['Accounts Receivable'] / scorecard['Net Revenue']) * 365
    scorecard['Days of Inventory on Hand'] = (scorecard['Inventory'] / scorecard['COGS']) * 365
    scorecard['Payables Period'] = (scorecard['Accounts Payable'] / scorecard['COGS']) * 365
    scorecard['Cash Cycle'] = scorecard['Days of Sales Outstanding'] + scorecard['Days of Inventory on Hand'] - scorecard['Payables Period']
    return scorecard




"""

Helper functions for the main functions below

"""


def standardize_date(date: str) -> str:
    for abbr, full in zip(calendar.month_abbr[1:], calendar.month_name[1:]):
        date = date.replace(abbr, full)
    return date


def custom_aggregator(series):
    first_val = series.iloc[0]
    for value in series[1:]:
        if pd.isna(first_val) and not pd.isna(value):
            first_val = value 
    return first_val


def retrieve_balance_income_cf_and_store_as_CSV(ticker, blank: bool = True):
    earnings_sheet = form_statement_for_all_available_years(ticker, "income_statement")
    balance_sheet = form_statement_for_all_available_years(ticker, "balance_sheet")
    cash_flow_sheet = form_statement_for_all_available_years(ticker, "cash_flow_statement")
    all_three_statements = pd.concat(
    [balance_sheet, earnings_sheet, cash_flow_sheet],
    keys=["balance_sheet", "earnings_sheet", "cash_flow_sheet"],
)
    if blank == True:
        all_three_statements = all_three_statements.replace(["None", np.NaN], "")
    save_dataframe_to_csv(cash_flow_sheet, "results", ticker, "cash_flow_statement", "annual")
    save_dataframe_to_csv(balance_sheet, "results", ticker,"balance_sheet", "annual")
    save_dataframe_to_csv(earnings_sheet, "results", ticker, "income_statement", "annual")
    save_dataframe_to_csv(all_three_statements, "results", ticker, "all_three_main_statements", "annual")
    return all_three_statements


def store_balance_income_cf_for_all_quarters_and_years(ticker):
    earnings_sheet = form_statement_for_all_available_years(ticker, "income_statement")
    balance_sheet = form_statement_for_all_available_years(ticker, "balance_sheet")
    cash_flow_sheet = form_statement_for_all_available_years(ticker, "cash_flow_statement")
    save_dataframe_to_csv(cash_flow_sheet, 'quarterly&annual_results', ticker, "cash_flow_statement", "annual")
    save_dataframe_to_csv(balance_sheet, 'quarterly&annual_results', ticker, "balance_sheet", "annual")
    save_dataframe_to_csv(earnings_sheet, 'quarterly&annual_results', ticker, "income_statement", "annual")
    earnings_sheet = form_statement_for_all_available_quarters(ticker, "income_statement")
    balance_sheet = form_statement_for_all_available_quarters(ticker, "balance_sheet")
    cash_flow_sheet = form_statement_for_all_available_quarters(ticker, "cash_flow_statement")
    save_dataframe_to_csv(cash_flow_sheet, 'quarterly&annual_results', ticker, "cash_flow_statement", "quarterly")
    save_dataframe_to_csv(balance_sheet, 'quarterly&annual_results', ticker, "balance_sheet", "quarterly")
    save_dataframe_to_csv(earnings_sheet, 'quarterly&annual_results', ticker, "income_statement", "quarterly")
    return None
 
    
def save_dataframe_to_csv(dataframe, folder_name, ticker, statement_name, frequency):
    directory_path = os.path.join(folder_name, ticker)
    os.makedirs(directory_path, exist_ok=True)
    file_path = os.path.join(directory_path, f"{statement_name}_{frequency}.csv")
    dataframe.to_csv(file_path)
    return None
    
    
def print_links_to_desired_statment(ticker, statement_name):
    statement_name = statement_name.lower()
    acc_series = get_10K_accessionNumbers_for_ticker(ticker)
    cik = get_cik_matching_ticker(ticker)
    for accession_number in acc_series:
        base_link = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession_number}"
        try:
            statement_file_names_dict = get_statement_file_names_in_filing_summary(ticker, accession_number)
            statement_keys_map = {
        'balance_sheet': [
            'balance sheet',
            'balance sheets',
            'statement of financial position',
            'consolidated balance sheets',
            'consolidated balance sheet',
            'consolidated financial position',
            'consolidated balance sheets - southern',
            'consolidated statements of financial position',
            'consolidated statement of financial position',
            'consolidated statements of financial condition',
            'combined and consolidated balance sheet',
            'condensed consolidated balance sheets',
            'consolidated balance sheets, as of december 31',
            'dow consolidated balance sheets',
            'consolidated balance sheets (unaudited)',
        ],
        'income_statement': [
            'income statement',
            'income statements',
            'statement of earnings (loss)',
            'statements of consolidated income',
            'consolidated statements of operations',
            'consolidated statement of operations', 
            'consolidated statements of earnings', 
            'consolidated statement of earnings',
            'consolidated statements of income', 
            'consolidated statement of income',
            'consolidated income statements',
            'consolidated income statement',
            'condensed consolidated statements of earnings',
            'consolidated results of operations',
            'consolidated statements of income (loss)',
            'consolidated statements of income - southern',
            'consolidated statements of operations and comprehensive income',
            'consolidated statements of comprehensive income',
        ],
        'cash_flow_statement': [
            'cash flows statement',
            'cash flows statements',
            'statement of cash flows',
            'statements of consolidated cash flows',
            'consolidated statements of cash flows',
            'consolidated statement of cash flows',
            'consolidated statement of cash flow',
            'consolidated cash flows statements',
            'consolidated cash flow statements',
            'condensed consolidated statements of cash flows',
            'consolidated statements of cash flows (unaudited)',
            'consolidated statements of cash flows - southern',
        ]
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
            
        except:
            continue
        print(statement_link)
    return None
    
    


def keep_numbers_and_decimals_only_in_string(mixed_string: str):
    num = "1234567890."
    allowed = list(filter(lambda x: x in num, mixed_string))
    return "".join(allowed)


def keep_letters_and_numbers_only_in_string(mixed_string: str):
    alpha_num = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ";
    allowed = list(filter(lambda x: x in alpha_num, mixed_string))
    return "".join(allowed)




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



def get_statement_using_pandas(ticker, accession_number, statement_name):
        soup = get_statement_soup(ticker, accession_number, statement_name)
        data = pd.read_html(str(soup))[0]
        return data


def rename_with_all_statement_labels(statement, ticker):
    accession_num_series = get_10K_accessionNumbers_for_ticker(ticker)
    for accession_num in accession_num_series:
        label_dict = get_label_dictionary(ticker, accession_num)
        if label_dict == None:
            break
        statement = rename_statement(statement, label_dict)
        print("Renamed with accession number: " + accession_num)
    return statement