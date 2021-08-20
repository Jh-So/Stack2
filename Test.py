import urllib.request
import json, requests
import pandas as pd
import csv
import pandas as pd
import yfinance as yf
import re

market_list = ["NYSE"]


for market in market_list:
    url = "https://api.stock.naver.com/stock/exchange/{}/marketValue?page=1&pageSize=20".format(market)
    data = json.loads(urllib.request.urlopen(url).read())

    total_count = data['totalCount']
    total_page_number = int(total_count / 20) + 1

    number = 0

    # for csv
    number_list = []
    symbol_code_list = []
    stock_name_list = []

    rows = []

    for page in range(1, 5):

        temp_url = "https://api.stock.naver.com/stock/exchange/{}/marketValue?page={}&pageSize=20".format(market,
            page)

        data = json.loads(urllib.request.urlopen(temp_url).read())
        stocks = data['stocks']

        for stock in stocks:
            row = []
            number += 1
            # print(number, stock['symbolCode'], stock['stockName'], stock['stockNameEng'])

            try:
                reutersCode = stock['reutersCode']
                url_description = "https://api.stock.naver.com/stock/{}/overview".format(reutersCode)
                print(url_description)
                data_description = json.loads(urllib.request.urlopen(url_description).read())
            except:
                print(reutersCode)
                print(stock['symbolCode'])


            row.append(number)
            row.append(stock['symbolCode'])
            row.append(stock['stockName'])
            row.append(stock['stockNameEng']) #chrome 개발자 도구 -> network -> fetch/xhr -> basic -> preview
            row.append(data_description['summary'])
            rows.append(row)

    df = pd.DataFrame(rows, columns=["Number", "Ticker", "KoreanTicker", "FullName", "Description"])
    df.to_csv("{}.csv".format(market), encoding="cp949", index=False)