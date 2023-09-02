import sys
import pytest
import pandas as pd
import time
import logging
sys.path.append('..')
from edgar_functions import get_10K_accessionNumbers_for_ticker, process_one_statement

logging.basicConfig(level=logging.INFO)
tickers = pd.read_html('https://en.wikipedia.org/wiki/S%26P_100')[2]

@pytest.mark.parametrize('ticker', tickers['Symbol'].tolist())
def test_process_one_statement_for_balance_sheet(ticker):
    accession_numbers = get_10K_accessionNumbers_for_ticker(ticker)
    assert not accession_numbers.empty, f"No accession numbers found for ticker {ticker}"

    for accession_number in accession_numbers:
        time.sleep(0.2)  # Respect rate limit
        df = process_one_statement(ticker, accession_number, 'balance_sheet')
        assert df is not None and not df.empty, f"Empty DataFrame for ticker {ticker} and accession number {accession_number}"
