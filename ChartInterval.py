

import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import datetime as dt


stock_1d = pd.read_csv("./AAPL_1d_all_data.csv")
stock_1w = pd.read_csv("./AAPL_1w_all_data.csv")
stock_1m_1d = pd.read_csv("./AAPL_1m_1days_data.csv")
stock_5m_1d = pd.read_csv("./AAPL_5m_1days_data.csv")
stock_5m_5d = pd.read_csv("./AAPL_5m_5days_data.csv")

stock_temp = stock_1w
# stock_temp = stock_temp[len(stock_temp)-30:]
plt.plot(stock_temp['Close'])
plt.show()











##resample
# stock_1d['Date'] = pd.to_datetime(stock_1d['Date'])
# stock_1d.set_index('Date', inplace = True)
# stock_1m['Date'] = pd.to_datetime(stock_1m['Date'])
# stock_1m.set_index('Date', inplace = True)

# plt.subplot(711)
# stock_5d = stock_1d
# stock_5d=stock_5d.resample(rule='5B').last()

# Graph_interval = {'1D' : '1T', '5D' : '5T', '1m' : 'B','3M' : 'B', '6M' : 'B', '1Y' : 'B','ALL' : 'W'}
# i = 0
# for axis, interval in Graph_interval.items():
#     i=i+1
#
#     plt.subplot(710 + i)
#     if i < 3 :
#         stock_temp = stock_1m
#     else :
#         stock_temp = stock_1d
#
#     stock_temp = stock_temp.resample(rule = interval).last()
#     print(stock_temp['Close'])
#
#     plt.plot(stock_temp['Close'])
#     plt.title("{}, data interval = {}".format(axis,interval))
#
# plt.show()
