import pandas as pd

def detect_anomalies(df):
    threshold = 2
    df['ctr'] = df['clicks'] / df['impressions']
    mean_ctr = df['ctr'].mean()
    std_ctr = df['ctr'].std()
    df['z_score'] = (df['ctr'] - mean_ctr) / std_ctr
    anomalies = df[df['z_score'].abs() > threshold]
    return anomalies
