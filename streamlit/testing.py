import os.path
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from edgar_functions import (
    form_statement_for_all_available_years,
    get_10K_accessionNumbers_for_ticker,
    get_label_dictionary,
    rename_statement,
)
from edgar_functions_V2 import *

ticker = "WSM"
statement = "income_statement"
st.set_page_config(layout="wide")

st.title("Annual Financial Statement Viewer")

ticker_input = st.text_input("Enter Ticker", ticker)
statement = st.selectbox(
    "Select Statement", ("income_statement", "balance_sheet", "cash_flow_statement")
)

if st.button("Get Statement"):
    try:
        first_accession_num = get_10K_accessionNumbers_for_ticker(ticker_input).iloc[0]
        labels = get_label_dictionary(ticker_input, first_accession_num)
        df = form_statement_for_all_available_years(ticker_input, statement)
        df = rename_statement(df, labels)
        df = df.fillna("")
        st.write(f"Displaying {statement} for {ticker_input}")
        st.dataframe(df, height=1000)

    except Exception as e:
        st.write(f"Error: {e}")
