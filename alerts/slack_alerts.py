import requests

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/your/webhook/url"

def send_slack_alert(message):
    payload = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    if response.status_code == 200:
        print("✅ Slack alert sent")
    else:
        print("❌ Failed to send alert:", response.text)
