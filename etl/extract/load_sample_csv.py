import pandas as pd

def load_sample_data(file_path="data/sample_campaign_data.csv"):
    df = pd.read_csv(file_path)
    return df
