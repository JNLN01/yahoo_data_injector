import yfinance as yf
import numpy as np
import pandas as pd

def download(ticker, start_date, end_date):
    df = yf.download(ticker, start=start_date, end=end_date)
    return df

df1 = download("EURUSD=X", "2003-12-1", "2023-03-06",)
df1 = df1.loc[:, ["Open", "Close"]]  # Sets out only Open and close prices in the dataset.
weekly_df1 = df1.resample("W").agg({'Open': 'first', 'Close': 'last'})
weekly_df1.head() #Above, filters data to weekly. Sunday open to Friday close.
print(weekly_df1.head) #prints the table for x instrument for y dates

#To be worked on; Rework options for the dataframe + manipulation options of said dataframe.
#User option to save the dataframe.

var = input("Do you want to save? ")
var = var.lower()   #forces user response to be lowercase.

if var == 'yes':
    df1.to_csv('yahoo_dataframe.csv')
    print("Dataframe saved as yahoo_dataframe.csv")

elif var == 'no':
   print("Not saved as CSV")

else:
    print('Incorrect Input. Try a yes or no')
