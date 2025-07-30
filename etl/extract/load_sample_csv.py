import pandas as pd

def load_sample_data():
    df = pd.read_csv("etl/extract/sample_data.csv")
    return df
