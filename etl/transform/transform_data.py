import pandas as pd

def transform_campaign_data(df: pd.DataFrame):
    # Fill NA with 0 for numeric columns
    df.fillna(0, inplace=True)

    # Ensure types
    df["clicks"] = df["clicks"].astype(int)
    df["impressions"] = df["impressions"].astype(int)
    df["conversions"] = df["conversions"].astype(int)
    df["cost"] = df["cost"].astype(float)

    # Calculate derived metrics
    df["ctr"] = (df["clicks"] / df["impressions"]).round(4)  # Click-through rate
    df["cpc"] = (df["cost"] / df["clicks"]).round(2)         # Cost per click
    df["roi"] = ((df["conversions"] * 10 - df["cost"]) / df["cost"]).round(2)  # Example: each conv = ₹10 revenue

    return df
