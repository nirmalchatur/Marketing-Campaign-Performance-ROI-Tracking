import pandas as pd

def normalize_data(df, platform):
    df['roi'] = (df['conversions'] * 100 - df['cost']) / df['cost']
    df['platform'] = platform
    return df
