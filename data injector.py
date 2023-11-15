import yfinance as yf
import numpy as np
import pandas as pd

def download(ticker, start_date, end_date):
    df = yf.download(ticker, start=start_date, end=end_date)
    return df
#                Asset   ,Start Date  , End Date
df1 = download("AZN.L", "2018-01-01", "2023-01-01",)
df1 = df1.loc[:, ["Open", "Close"]]  # Sets out only Open and close prices in the dataset.
weekly_df1 = df1.resample("D").agg({'Open': 'first', 'Close': 'last'})
weekly_df1.head() #Above, filters data to weekly (W). Sunday open to Friday close.
print(weekly_df1.head) #prints the dataframe for x instrument for y date range

#To be worked on; Rework options for the dataframe + manipulation options of said dataframe.

#Saves the dataframe as .csv
df1.to_csv('yahoo_DF.csv', sep=',', index=False, encoding='utf-8')

