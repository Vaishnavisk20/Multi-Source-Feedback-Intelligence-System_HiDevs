import pandas as pd

def calculate_trend(df):

    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    trend = df.groupby([df["date"].dt.date,"sentiment"]).size().unstack()

    return trend