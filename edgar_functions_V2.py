import json
import logging
from datetime import datetime

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import etree

from name_mappings import (
    balance_sheet_mapping,
    cash_flow_mapping,
    income_statement_mapping,
)

pd.set_option("display.max_rows", 600)
pd.options.display.float_format = (
    lambda x: "{:,.0f}".format(x) if int(x) == x else "{:,.2f}".format(x)
)
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
    tickers_json = requests.get(
        "https://www.sec.gov/files/company_tickers.json", headers=headers
    ).json()

    for company in tickers_json.values():
        if company["ticker"] == ticker:
            cik = str(company["cik_str"]).zfill(10)
            return cik
    raise ValueError(f"Ticker {ticker} not found")


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


def get_annual_edgar_facts_from_downloaded_json(cik):
    json_file = f"companyfacts/CIK{cik}.json"
    with open(json_file, "r") as f:
        json_data = json.load(f)
    us_gaap_facts = json_data.get("facts", {}).get("us-gaap", {})
    full_dataframe = pd.DataFrame()
    for i, (fact, details) in enumerate(us_gaap_facts.items()):
        units = details.get("units", {})
        unit_key = list(units.keys())[0] if units else None
        if unit_key:
            data = units[unit_key]
            temp_df = pd.DataFrame(data)

            if "frame" in temp_df.columns:
                temp_df = temp_df[temp_df["frame"].notnull()]
                if not temp_df.empty:
                    temp_df.loc[:, "fact"] = fact

                full_dataframe = pd.concat([full_dataframe, temp_df])
    return full_dataframe


def process_and_aggregate_annual_data(ticker):
    cik = get_cik(ticker)
    frames_to_include = [
        "CY2007",
        "CY2008",
        "CY2009",
        "CY2010",
        "CY2011",
        "CY2012",
        "CY2013",
        "CY2014",
        "CY2015",
        "CY2016",
        "CY2017",
        "CY2018",
        "CY2019",
        "CY2020",
        "CY2021",
        "CY2022",
        "CY2023",
    ]
    filings_df = get_submission_data_for_ticker(ticker, only_filings_df=True)
    full_facts = get_annual_edgar_facts_from_downloaded_json(cik)
    full_facts["end"] = pd.to_datetime(full_facts["end"])
    full_facts["filed"] = pd.to_datetime(full_facts["filed"])
    pivot_table = pd.pivot_table(
        full_facts, index=["end", "frame"], columns=["fact"], values=["val"]
    )

    # Filter DataFrame based on frames_to_include
    filtered_df = pivot_table.loc[
        pivot_table.index.get_level_values(1).isin(frames_to_include)
    ]

    # Get unique dates
    unique_dates = filtered_df.index.get_level_values(0).unique()

    # Filter DataFrame again based on unique_dates
    final_filtered_df = pivot_table.loc[(unique_dates, slice(None)), :].sort_index(
        level=1, ascending=True
    )
    final_filtered_df.columns = final_filtered_df.columns.droplevel(0)

    # Insert additional columns
    final_filtered_df.insert(
        0, "Year", final_filtered_df.index.get_level_values(1).str[2:6]
    )
    final_filtered_df.insert(
        1, "Period End", final_filtered_df.index.get_level_values(0)
    )

    # Group by 'Year' and take the first entry for each group
    aggregated_df = final_filtered_df.groupby("Year").first()

    # Calculate extended filing dates
    desired_length = len(aggregated_df.index)
    filing_dates = filings_df[filings_df["form"] == "10-K"]["filingDate"]
    filing_dates = pd.to_datetime(filing_dates)
    average_time_delta = filing_dates.diff().dropna().mean()
    current_date = filing_dates.min()

    extended_dates = []
    for _ in range(desired_length - len(filing_dates)):
        next_date = current_date + average_time_delta
        extended_dates.append(next_date)
        current_date = next_date

    # Insert 'Filing Date' column
    extended_dates_series = pd.Series(extended_dates, name="Filing Date")
    final_extended_filing_dates = (
        pd.concat([filing_dates, extended_dates_series])
        .sort_values()
        .reset_index(drop=True)
    )
    final_extended_filing_dates = final_extended_filing_dates.dt.strftime("%Y-%m-%d")
    aggregated_df.insert(1, "Filing Date", final_extended_filing_dates.values)
    aggregated_df["Filing Date"] = pd.to_datetime(aggregated_df["Filing Date"])

    # Convert all column names to strings and drop NaN columns
    aggregated_df.columns = aggregated_df.columns.map(str)
    aggregated_df = aggregated_df.dropna(axis=1, how="all")

    return aggregated_df


def generate_reverse_mapping_and_rename(df, mapping_dict):
    reverse_mapping = {}
    for new_col, old_cols in mapping_dict.items():
        for old_col in old_cols:
            suffix = old_col.split("_")[-1].lower()
            reverse_mapping[suffix] = new_col

    # Rename the columns in a case-insensitive manner
    new_columns = []
    for col in df.columns:
        col_lower = col.lower()
        if col_lower in reverse_mapping:
            new_columns.append((reverse_mapping[col_lower], col))
        else:
            new_columns.append((col, ""))

    renamed_df = df.copy()
    renamed_df.columns = pd.MultiIndex.from_tuples(new_columns)

    return renamed_df


def get_changed_columns(statement_mapping_dict, aggregated_df):
    renamed_df = generate_reverse_mapping_and_rename(
        aggregated_df, statement_mapping_dict
    )
    original_columns = set(aggregated_df.columns)
    new_columns = set([col[0] for col in renamed_df.columns])
    changed_columns = new_columns - original_columns
    changed_df = renamed_df.loc[
        :, [col for col in renamed_df.columns if col[0] in changed_columns]
    ]
    changed_df.index.name = None
    changed_df.columns.names = [None, "Gaap Name"]

    return changed_df


def combine_or_add_columns(df, cols, add_instead=False, replace_zero=False):
    if not cols:
        return None

    primary_col = None
    for col in cols:
        if col in df.columns:
            primary_col = df[col]
            break

    if primary_col is None:
        return None

    if len(cols) == 1:
        return primary_col

    for col in cols[1:]:
        if col in df.columns:
            # Skip if the column contains all NaN values
            if df[col].isna().all():
                continue

            if add_instead:
                primary_col = primary_col.add(df[col], fill_value=0).combine_first(
                    primary_col.combine_first(df[col])
                )
            else:
                if replace_zero:
                    primary_col = primary_col.mask(primary_col == 0).combine_first(
                        df[col]
                    )
                else:
                    primary_col = primary_col.combine_first(df[col])

    return primary_col
