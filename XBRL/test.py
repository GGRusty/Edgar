import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../wsm_annual_edgar_facts.csv")

Assets__USD = data['Assets__USD']
Assets__USD.index = data['end']

Liabilities__USD = data['Liabilities__USD']
Liabilities__USD.index = data['end']

StockholdersEquity__USD = data['StockholdersEquity__USD']
StockholdersEquity__USD.index = data['end']

NetIncomeLoss__USD = data['NetIncomeLoss__USD']
NetIncomeLoss__USD.index = data['end']

CommonStockValue__USD = data['CommonStockValue__USD'] * 100
CommonStockValue__USD.index = data['end']


important_data = pd.DataFrame()
important_data['Liabilities'] = Liabilities__USD
important_data['Assets'] = Assets__USD
important_data['StockholdersEquity'] = StockholdersEquity__USD
important_data['NetIncome'] = NetIncomeLoss__USD
important_data['CommonShares'] = CommonStockValue__USD

important_data['NI_PerShare'] = important_data['NetIncome'] / important_data['CommonShares']

important_data['L_PerShare'] = important_data['Liabilities'] / important_data['CommonShares']
