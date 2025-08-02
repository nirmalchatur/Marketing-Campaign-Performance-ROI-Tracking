import requests
import os
from dotenv import load_dotenv

load_dotenv()

def send_slack_alert(message):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        raise ValueError("SLACK_WEBHOOK_URL not found in .env")

    payload = {"text": message}
    response = requests.post(webhook_url, json=payload)

    if response.status_code == 200:
        print("✅ Slack alert sent successfully.")
    else:
        print(f"❌ Slack alert failed: {response.status_code} — {response.text}")
