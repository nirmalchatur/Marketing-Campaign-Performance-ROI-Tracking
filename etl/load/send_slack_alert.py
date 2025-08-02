import requests
import os

def send_slack_alert(message):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        raise ValueError("SLACK_WEBHOOK_URL is not set in environment variables.")

    payload = {"text": message}
    response = requests.post(webhook_url, json=payload)

    if response.status_code == 200:
        print("✅ Slack alert sent successfully.")
    else:
        print(f"❌ Failed to send Slack alert: {response.status_code}, {response.text}")
