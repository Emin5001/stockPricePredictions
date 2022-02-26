import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

apple_stock_data = pd.read_csv('/Users/eminn/PycharmProjects/stockPricePredictions/data/APPL.csv')

"""
This code block formats the apple_stock_data
variable into a table that can be used to 
extract the columns with the information that we need,
such as Date, Open Price, and Close Price.
"""
apple_stock_data = apple_stock_data[['Date', 'Open', 'Close']]
apple_stock_data['Date'] = pd.to_datetime(apple_stock_data['Date'].apply(lambda x : x.split()[0]))
apple_stock_data.set_index('Date', drop=True, inplace=True)
print(apple_stock_data.head())
