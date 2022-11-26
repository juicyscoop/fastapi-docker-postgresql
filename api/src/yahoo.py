from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
yf.pdr_override()
import pandas as pd

# ticker_list=[‘DJIA’, ‘DOW’, ‘LB’, ‘EXPE’, ‘PXD’, ‘MCHP’, ‘CRM’, ‘JEC’ , ‘NRG’, ‘HFC’, ‘NOW’]

def get_yahoo_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    data = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
    return data