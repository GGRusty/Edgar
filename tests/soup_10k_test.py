# this test is to make sure that the get_statement_soup function is working properly
# it takes around 6 minutes to run
import sys
import pytest
import pandas as pd
import time
sys.path.append('..')
from edgar_functions import get_statement_soup, get_10K_accessionNumbers_for_ticker

tickers = pd.read_html('https://en.wikipedia.org/wiki/S%26P_100')[2]

@pytest.mark.parametrize('ticker', tickers['Symbol'].tolist())
def test_get_statement_soup(ticker):
    accession_number = get_10K_accessionNumbers_for_ticker(ticker)[0]

    for statement in ['balance_sheet', 'income_statement', 'cash_flow_statement']:
        time.sleep(0.2)
        soup = get_statement_soup(ticker, accession_number, statement)
        assert soup is not None, f"Failed to get {statement} for {ticker}"