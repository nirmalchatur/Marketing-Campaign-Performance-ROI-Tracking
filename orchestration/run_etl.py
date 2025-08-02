import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from etl.extract.load_sample_csv import load_sample_data
from etl.transform.transform_data import transform_campaign_data
from etl.load.load_to_db import load_to_mongo
from etl.load.send_slack_alert import send_slack_alert  # Add this line
from dotenv import load_dotenv

load_dotenv()  # Load your .env file

if __name__ == "__main__":
    # ETL steps
    raw_df = load_sample_data()
    transformed_df = transform_campaign_data(raw_df)
    load_to_mongo(transformed_df)
    print("✅ Data loaded into MongoDB collection: campaign_metrics")

    # ROI anomaly detection
    anomalies = transformed_df[transformed_df["ROI (%)"] < 10]  # You can change threshold

    if not anomalies.empty:
        for _, row in anomalies.iterrows():
            msg = (
                f"🚨 *ROI Anomaly Detected!*\n"
                f"Platform: {row['platform']}\n"
                f"Campaign: {row['campaign_name']}\n"
                f"ROI: {row['ROI (%)']:.2f}%\n"
                f"Date: {row['date']}"
            )
            send_slack_alert(msg)
    else:
        print("✅ No ROI anomalies detected.")
