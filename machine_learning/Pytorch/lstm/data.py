import os

import pandas as pd

import pandas_ta as ta

pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.width', 1000)  # 调整显示宽度防止换行


def process_type1(file_path, period=10):
    print(f"开始读取文件 {file_path}")
    df = pd.read_csv(file_path)
    print(df.dtypes)
    print(df.columns)
    df['dateTime'] = pd.to_datetime(df['Date-Time'], errors='coerce')
    # 删除列
    df = df.drop(['#RIC', 'Domain', "GMT Offset", 'Type', 'No. Asks', 'No. Bids', 'Date-Time',"Alias Underlying RIC"], axis=1)
    # 计算中间价ohlc
    df['Open Mid'] = ((df['Open Bid'] + df['Open Ask']) / 2).round(5)
    df['High Mid'] = ((df['High Bid'] + df['High Ask']) / 2).round(5)
    df['Low Mid'] = ((df['Low Bid'] + df['Low Ask']) / 2).round(5)
    df['close_mid'] = ((df['Close Bid'] + df['Close Ask']) / 2).round(5)
    # 删除买卖价
    df = df.drop(['Open Bid', 'High Bid', 'Low Bid', 'Close Bid', 'Open Ask', 'High Ask', 'Low Ask', 'Close Ask',"dateTime" ],
                 axis=1)

    # 计算指标
    # 计算ma值
    df['MA20'] = (ta.sma(df['close_mid'], length=period)).round(5)

    # 计算 diff 值
    df['close_diff'] = (df['close_mid'].diff()).round(5)
    print(df.head())
    df["close_next"] = df["close_mid"].shift(-1)
    # 删除最后一行
    df = df[period:-1]
    print(df.dtypes)
    print(df.columns)
    print(df.head())
    base_name=os.path.basename(file_path).split('.')[0]
    df.to_csv(f'{base_name}_{period}.csv', index=False, encoding='utf_8_sig')


# file = "eur-22-24-1m.csv"
file = r"C:\Users\sutut\Desktop\data\eur-22-24-5m.csv"

process_type1(file)
