import psycopg2
import os
from dotenv import load_dotenv

load_dotenv("config/config.env")

def load_data(df):
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    cur = conn.cursor()
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO campaign_metrics (campaign_id, platform, impressions, clicks, cost, conversions, roi, date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, CURRENT_DATE)
        """, (row['campaign_id'], row['platform'], row['impressions'], row['clicks'],
              row['cost'], row['conversions'], row['roi']))
    conn.commit()
    cur.close()
    conn.close()
