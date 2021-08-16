import yfinance as yf
import pandas as pd
import os.path


market_list = ["NYSE", "NASDAQ","AMEX"]

for market in market_list:
    TickerList = pd.read_csv('./Input/{}.csv'.format(market), encoding = 'cp949', index_col='Number')

    print(" market : {}".format(market))

    for i in range(len(TickerList.index)):

        ticker = TickerList.iloc[i]
        ticker = ticker[0] #series type을 문자열로 변경

        Curpath =os.getcwd() + '/Output/{}/'.format(market)
        # print(Curpath)
        filename = '{}.csv'.format(ticker)

        if os.path.isfile((Curpath+filename)) : #이미 있는 파일은 건너뜀
            print("pass!!")
            continue
        else :
            # get stock info
            hist = yf.download(ticker)

            path = './Output/{}'.format(market)
            if not os.path.isdir(path):
                os.mkdir(path)
            hist.to_csv(path + '/{}'.format(filename), index = True, encoding = 'cp949')

