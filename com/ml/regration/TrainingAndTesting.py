import math
import pandas as pd
import quandl as qd
from sklearn import preprocessing, cross_decomposition, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import  numpy as np

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
print('forcast_out', forcast_out)
df['predicted_value'] = df[forcast_col].shift(-forcast_out)
df.dropna(inplace=True)
# print(df.head())

x = np.array(df.drop(['predicted_value'], 1))
y = np.array(df['predicted_value'])
x = preprocessing.scale(x)
y = np.array(df['predicted_value'])

# create train and test cases

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# select the algorith to find out the accuracy

clt = LinearRegression()
clt.fit(x_train, y_train)
accuracy = clt.score(x_test, y_test)

print('accuracy', accuracy)
