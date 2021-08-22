import yfinance as yf
import pandas as pd

AAPL = yf.Ticker("AAPL")
df = AAPL.history(period="max",interval="1wk")
df = pd.DataFrame(df)
df.to_csv("./{}_1w_all_data.csv".format("AAPL"), index = True, encoding = 'cp949')
