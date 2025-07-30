from etl.extract.google_ads import fetch_google_ads_data
from etl.transform.normalize_data import normalize_data
from etl.load.load_to_db import load_data
from alerts.detect_anomalies import detect_anomalies
from alerts.send_alerts import send_slack_alert
import pandas as pd

def run_pipeline():
    raw_data = fetch_google_ads_data()
    df = pd.DataFrame(raw_data)
    df = normalize_data(df, "GoogleAds")
    load_data(df)

    anomalies = detect_anomalies(df)
    if not anomalies.empty:
        send_slack_alert("⚠️ Anomaly detected in Google Ads campaigns!")

if __name__ == "__main__":
    run_pipeline()
