import os.path
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from edgar_functions_V2 import *
from edgar_functions import form_statement_for_all_available_years
import streamlit as st

ticker = "WSM"
statement = "income_statement"

st.title("EDGAR Filing Viewer")

st.write(form_statement_for_all_available_years(ticker, statement))
