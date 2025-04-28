import pandas as pd


def process_type1(file_path):
    df = pd.read_csv(file_path)
    print(df.dtypes)
    print(df.columns)
    df['dateTime'] = pd.to_datetime(df['Date-Time'], errors='coerce')
    df = df.drop(['#RIC', 'Domain', "GMT Offset", 'Type', 'No. Asks', 'No. Bids', 'Date-Time'], axis=1)
    df['Open Mid'] = ((df['Open Bid'] + df['Open Ask']) / 2).round(5)
    df['High Mid'] = ((df['High Bid'] + df['High Ask']) / 2).round(5)
    df['Low Mid'] = ((df['Low Bid'] + df['Low Ask']) / 2).round(5)
    df['Close Mid'] = ((df['Close Bid'] + df['Close Ask']) / 2).round(5)
    df = df.drop(['Open Bid', 'High Bid', 'Low Bid', 'Close Bid','Open Ask', 'High Ask', 'Low Ask', 'Close Ask',], axis=1)

    print(df.dtypes)
    print(df.columns)
    print(df.head())


file = "eur-22-24-1m.csv"

process_type1(file)
