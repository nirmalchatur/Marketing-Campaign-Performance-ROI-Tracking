import pandas as pd

def transform_campaign_data(df):
    # Ensure numeric columns
    df["clicks"] = df["clicks"].astype(int)
    df["impressions"] = df["impressions"].astype(int)
    df["cost"] = df["cost"].astype(float)
    df["conversions"] = df["conversions"].astype(int)

    # Compute CTR
    df["CTR (%)"] = (df["clicks"] / df["impressions"]) * 100

    # Compute ROI
    # Assuming each conversion gives $50 in revenue
    df["ROI (%)"] = ((df["conversions"] * 50 - df["cost"]) / df["cost"]) * 100

    return df

