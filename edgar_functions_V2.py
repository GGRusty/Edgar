import requests
import logging
import numpy as np
import pandas as pd
from lxml import etree
from bs4 import BeautifulSoup

headers = {"User-Agent": "russ@sunriseanalysis.com"}

statement_keys_map = {
    "balance_sheet": [
        "balance sheet",
        "balance sheets",
        "statement of financial position",
        "consolidated balance sheets",
        "consolidated balance sheet",
        "consolidated financial position",
        "consolidated balance sheets - southern",
        "consolidated statements of financial position",
        "consolidated statement of financial position",
        "consolidated statements of financial condition",
        "combined and consolidated balance sheet",
        "condensed consolidated balance sheets",
        "consolidated balance sheets, as of december 31",
        "dow consolidated balance sheets",
        "consolidated balance sheets (unaudited)",
    ],
    "income_statement": [
        "income statement",
        "income statements",
        "statement of earnings (loss)",
        "statements of consolidated income",
        "consolidated statements of operations",
        "consolidated statement of operations",
        "consolidated statements of earnings",
        "consolidated statement of earnings",
        "consolidated statements of income",
        "consolidated statement of income",
        "consolidated income statements",
        "consolidated income statement",
        "condensed consolidated statements of earnings",
        "consolidated results of operations",
        "consolidated statements of income (loss)",
        "consolidated statements of income - southern",
        "consolidated statements of operations and comprehensive income",
        "consolidated statements of comprehensive income",
    ],
    "cash_flow_statement": [
        "cash flows statement",
        "cash flows statements",
        "statement of cash flows",
        "statements of consolidated cash flows",
        "consolidated statements of cash flows",
        "consolidated statement of cash flows",
        "consolidated statement of cash flow",
        "consolidated cash flows statements",
        "consolidated cash flow statements",
        "condensed consolidated statements of cash flows",
        "consolidated statements of cash flows (unaudited)",
        "consolidated statements of cash flows - southern",
    ],
}


def get_cik(ticker, headers=headers):
    """
    Get the CIK for a given ticker.

    Args:
        ticker (str): The ticker symbol of the company.

    Returns:
        str: The CIK for the company.

    Raises:
        ValueError: If ticker is not a string.
    """
    ticker = ticker.upper().replace(".", "-")
    headers = headers
    tickers_json = requests.get(
        "https://www.sec.gov/files/company_tickers.json", headers=headers
    )
    cik_df = pd.DataFrame.from_dict(tickers_json.json(), orient="index")
    cik_df["cik_str"] = cik_df["cik_str"].astype(str).str.zfill(10)
    cik = cik_df[cik_df["ticker"] == ticker]["cik_str"].values[0]
    return cik


def get_submission_data_for_ticker(ticker, headers=headers, only_filings_df=False):
    """
    Get the data in json form for a given ticker. For example: 'cik', 'entityType', 'sic', 'sicDescription', 'insiderTransactionForOwnerExists', 'insiderTransactionForIssuerExists', 'name', 'tickers', 'exchanges', 'ein', 'description', 'website', 'investorWebsite', 'category', 'fiscalYearEnd', 'stateOfIncorporation', 'stateOfIncorporationDescription', 'addresses', 'phone', 'flags', 'formerNames', 'filings'

    Args:
        ticker (str): The ticker symbol of the company.

    Returns:
        json: The submissions for the company.

    Raises:
        ValueError: If ticker is not a string.
    """
    cik = get_cik(ticker)
    headers = headers
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    company_json = requests.get(url, headers=headers).json()
    if only_filings_df:
        company_filings_df = pd.DataFrame(company_json["filings"]["recent"])
        return company_filings_df
    else:
        return company_json


def get_filtered_filings(
    ticker, headers=headers, ten_k=True, just_accession_numbers=False
):
    company_filings_df = get_submission_data_for_ticker(
        ticker, headers, only_filings_df=True
    )
    if ten_k:
        df = company_filings_df[company_filings_df["form"] == "10-K"]
    else:
        df = company_filings_df[company_filings_df["form"] == "10-Q"]
    if just_accession_numbers:
        df["reportDate"] = pd.to_datetime(df["reportDate"])
        df.set_index("reportDate", inplace=True)
        accession_df = df["accessionNumber"]
        accession_df = accession_df.str.replace("-", "")
        return accession_df
    else:
        return df


def get_facts(ticker, headers=headers):
    cik = get_cik(ticker)
    headers = headers
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
    company_facts = requests.get(url, headers=headers).json()
    company_facts_df = pd.DataFrame(company_facts["facts"]["us-gaap"])
    return company_facts_df


def get_explored_facts(ticker, quarterly=False):
    facts = get_facts(ticker).T
    facts = facts["units"]
    facts_dict = facts.to_dict()
    rows = []
    for account_key, account_values in facts_dict.items():
        for unit_key, unit_values in account_values.items():
            for item in unit_values:
                row = {"account_key": account_key, "unit_key": unit_key}
                row.update(item)
                rows.append(row)
    df = pd.DataFrame(rows)
    if quarterly:
        ten_q = get_filtered_filings(ticker, ten_k=False)
        facts = df[df["accn"].isin(ten_q["accessionNumber"])]
        facts = facts[facts["filed"].isin(ten_q["filingDate"])]
        facts = facts.dropna(subset=["frame"])
        facts_pivot = facts.pivot_table(
            index="filed", columns="account_key", values="val"
        ).sort_index(ascending=False)
        return facts_pivot
    else:
        ten_k = get_filtered_filings(ticker, ten_k=True)
        facts = df[df["accn"].isin(ten_k["accessionNumber"])]
        facts = facts[facts["filed"].isin(ten_k["filingDate"])]
        facts = facts.dropna(subset=["frame"])
        facts_pivot = facts.pivot_table(
            index="filed", columns="account_key", values="val"
        ).sort_index(ascending=False)
        return facts_pivot


def get_statement_file_names_in_filing_summary(
    ticker, accession_number, headers=headers
):
    cik = get_cik(ticker)
    base_link = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession_number}"
    filing_summary_link = f"{base_link}/FilingSummary.xml"
    headers = headers
    filing_summary_response = requests.get(
        filing_summary_link, headers=headers
    ).content.decode("utf-8")
    filing_summary_soup = BeautifulSoup(filing_summary_response, "lxml-xml")
    statement_file_names_dict = {}

    for report in filing_summary_soup.find_all("Report"):
        short_name_tag = report.find("ShortName")
        long_name_tag = report.find("LongName")
        html_file_name_tag = report.find("HtmlFileName")
        xml_file_name_tag = report.find("XmlFileName")
        file_name = (
            html_file_name_tag.text
            if html_file_name_tag
            else xml_file_name_tag.text
            if xml_file_name_tag
            else None
        )

        if (
            long_name_tag
            and short_name_tag
            and file_name
            and "Statement" in long_name_tag.text
        ):
            short_name = short_name_tag.text.lower()
            statement_file_names_dict[short_name] = file_name

    return statement_file_names_dict


def get_statement_soup(
    ticker,
    accession_number,
    statement_name,
    headers=headers,
    statement_keys_map=statement_keys_map,
):
    """
    the statement_name should be one of the following:
    'balance_sheet'
    'income_statement'
    'cash_flow_statement'
    """
    cik = get_cik(ticker)
    statement_name = statement_name.lower()
    headers = headers
    base_link = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession_number}"
    statement_file_name_dict = get_statement_file_names_in_filing_summary(
        ticker, accession_number
    )
    statement_link = None
    for possible_key in statement_keys_map.get(statement_name, [statement_name]):
        try:
            statement_link = f"{base_link}/{statement_file_name_dict[possible_key]}"
            break
        except KeyError:
            continue

    if statement_link is None:
        raise ValueError(f"Could not find statement file name for {statement_name}")

    statement_response = requests.get(statement_link, headers=headers)
    if statement_link.endswith(".xml"):
        soup = BeautifulSoup(
            statement_response.content, "lxml-xml", from_encoding="utf-8"
        )
    else:
        soup = BeautifulSoup(statement_response.content, "lxml")

    return soup
