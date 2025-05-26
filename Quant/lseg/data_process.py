import pandas as pd
import mplfinance as mpf
import plotly.graph_objects as go
pd.set_option('display.max_rows', None)


def process_type1(file_path,period=10):
    df = pd.read_csv(file_path)
    print(df.dtypes)
    print(df.columns)
    df['dateTime'] = pd.to_datetime(df['Date-Time'], errors='coerce')
    df = df.drop(['#RIC', 'Domain', "GMT Offset", 'Type', 'No. Asks', 'No. Bids', 'Date-Time'], axis=1)
    df['Open'] = ((df['Open Bid'] + df['Open Ask']) / 2).round(5)
    df['High'] = ((df['High Bid'] + df['High Ask']) / 2).round(5)
    df['Low'] = ((df['Low Bid'] + df['Low Ask']) / 2).round(5)
    df['Close'] = ((df['Close Bid'] + df['Close Ask']) / 2).round(5)
    df = df.drop(['Open Bid', 'High Bid', 'Low Bid', 'Close Bid','Open Ask', 'High Ask', 'Low Ask', 'Close Ask','Alias Underlying RIC'], axis=1)

    df.set_index('dateTime', inplace=True)
    df.to_csv("5min.csv")
    df.sort_index(inplace=True)
    print(df.head(10))

    # 计算1小时的bar
    df = df.resample('H').agg({
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last'
    })
    # df=df.reset_index(drop=True)

    df["close_next"] = df["Close"].shift(-1)
    # 删除最后一行
    df = df[1:-1]
    print(df.dtypes)
    print(df.columns)
    print(df.head(100))
    # df.to_csv('eur-22-24-1H.csv', index=False,  encoding='utf-8-sig')
    df.to_csv('eur-22-24-1H_T.csv', index=True,  encoding='utf-8-sig')

# file = "eur-22-24-1m.csv"
file = r"C:\Users\sutut\Desktop\data\eur-22-24-5m.csv"

process_type1(file)
