import math

import pandas as pd
import quandl as qd

df = qd.get('WIKI/GOOGL') # get dataset from quandl
# print the dataset

df = df[['Open', 'High', 'Low', 'Adj. Close', 'Adj. Volume']]
df['HighLow_Change'] = ((df['High'] - df['Low']) / df['Low']) * 100.00
df['Daily_Change'] = ((df['High'] - df['Open']) / df['Open']) * 100.00

df = df[['Open', 'High', 'Low', 'Adj. Close', 'HighLow_Change', 'Daily_Change']]

# predict next days stock price

forcast_col = 'High'
df.fillna(-99999, inplace=True)  # fill null values with predefined value
forcast_out = int(math.ceil(0.001*len(df)))
df['predicted_value'] = df[forcast_col].shift(-forcast_out)
df.dropna(inplace=True)
print(df.head())

