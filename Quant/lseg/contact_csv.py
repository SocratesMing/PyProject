import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


def contact_data(file_senti: str = None, file_tick: str = None, senti_fields: list = []):
    # 处理tick数据
    df = pd.read_csv(file_tick)
    print(df.shape)
    df['dateTime'] = pd.to_datetime(df['Date-Time'], errors='coerce')
    df = df.drop(['#RIC', 'Domain', "GMT Offset", 'Type', 'No. Asks', 'No. Bids', 'Date-Time'], axis=1)
    df['Open'] = ((df['Open Bid'] + df['Open Ask']) / 2).round(5)
    df['High'] = ((df['High Bid'] + df['High Ask']) / 2).round(5)
    df['Low'] = ((df['Low Bid'] + df['Low Ask']) / 2).round(5)
    df['Close'] = ((df['Close Bid'] + df['Close Ask']) / 2).round(5)
    df = df[['dateTime', 'Open', 'High', 'Low', 'Close']]

    # 计算1小时的bar
    df.set_index('dateTime', inplace=True)
    df.sort_index(inplace=True)
    df = df.resample('h').agg({
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last'
    })
    # df = df.reset_index(drop=True)

    df["close_next"] = df["Close"].shift(-1)
    # 删除最后一行
    df = df[1:-1]

    print(df.head(10))

    # 处理情绪数据
    df1 = pd.read_csv(file_senti)

    df1['dateTime'] = pd.to_datetime(df1['windowTimestamp'], errors='coerce')

    df1 = df1[df1['dataType'] == 'News']
    res_col=['dateTime']
    res_col.extend(senti_fields)
    df1 = df1[res_col]

    df1.set_index('dateTime', inplace=True)
    print(df1.head(10))

    # 拼接两个数据
    df_res = df.join(df1, how='inner').reset_index()

    #
    cols = list(df_res.columns)
    cols.remove('close_next')  # 移除原列
    cols.append('close_next')  # 添加到末尾

    df_res = df_res[cols]
    df_res=df_res.reset_index(drop=True)
    df_res = df_res.drop(['dateTime'], axis=1)

    print("结果矩阵")
    print(df_res.head(10))
    df_res.to_csv("senti_pD.csv",index=False)


file_senti = r"C:\Users\sutut\Desktop\data\EUR_hou.csv"
file_tick = r"C:\Users\sutut\Desktop\data\eur-22-24-5m.csv"

contact_data(file_senti, file_tick, senti_fields=['sentiment', 'priceDirection'])
