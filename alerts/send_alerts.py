import requests
import os
from dotenv import load_dotenv

load_dotenv("config/config.env")

def send_slack_alert(message):
    url = "https://slack.com/api/chat.postMessage"
    headers = {"Authorization": f"Bearer {os.getenv('SLACK_TOKEN')}"}
    payload = {
        "channel": os.getenv("SLACK_CHANNEL"),
        "text": message
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.ok
