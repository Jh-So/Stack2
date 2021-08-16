import urllib.request
import json
import pandas as pd
import csv
import pandas as pd
import re
import yfinance as yf

market_list = ["NYSE", "NASDAQ","AMEX"]


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

    for page in range(1, total_page_number + 1):

        temp_url = "https://api.stock.naver.com/stock/exchange/{}/marketValue?page={}&pageSize=20".format(market,
            page)
        data = json.loads(urllib.request.urlopen(temp_url).read())
        stocks = data['stocks']

        for stock in stocks:
            row = []
            number += 1
            # print(number, stock['symbolCode'], stock['stockName'], stock['stockNameEng'])

            try:
                ticker = stock['symbolCode']
                ticker = re.sub("\.","",ticker)
                url_description = "https://api.stock.naver.com/stock/{}/overview".format(ticker)
                # print(url_description)
                data_description = json.loads(urllib.request.urlopen(url_description).read())
            except:
                try:    # ticker가 없는경우 마지막 글자를 소문자로 바꿈. ex) BRKb
                    ticker_ = list(ticker)
                    ticker_[-1] = ticker[-1].lower()
                    ticker_ = "".join(ticker_)
                    # print(ticker_)
                    url_description = "https://api.stock.naver.com/stock/{}/overview".format(ticker_)
                    # print(url_description)
                    data_description = json.loads(urllib.request.urlopen(url_description).read())

                except:
                    try : # 어떤 티커는 끝에 .K가 붙음 ex) BABA.K
                        url_description = "https://api.stock.naver.com/stock/{}.K/overview".format(ticker)
                        # print(url_description)
                        data_description = json.loads(urllib.request.urlopen(url_description).read())
                        
                    except : # 규칙성 없으면 메모하고 수동기입 필요
                        print(ticker)
                        continue

            row.append(number)
            row.append(stock['symbolCode'])
            row.append(stock['stockName'])
            row.append(stock['stockNameEng']) #chrome 개발자 도구 -> network -> fetch/xhr -> basic -> preview
            row.append(data_description['summary'])
            rows.append(row)

    df = pd.DataFrame(rows, columns=["Number", "Ticker", "KoreanName", "FullName", "Description"])
    df.to_csv("{}.csv".format(market), encoding="cp949", index=False)

    # commit test