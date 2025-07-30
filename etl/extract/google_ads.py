from google.ads.googleads.client import GoogleAdsClient
import os

def fetch_google_ads_data():
    client = GoogleAdsClient.load_from_storage("config/google-ads.yaml")
    ga_service = client.get_service("GoogleAdsService")

    query = """
        SELECT campaign.id, campaign.name, metrics.clicks, metrics.impressions,
               metrics.average_cpc, metrics.conversions, metrics.cost_micros
        FROM campaign
        WHERE segments.date DURING LAST_7_DAYS
    """

    response = ga_service.search(customer_id="YOUR_CUSTOMER_ID", query=query)
    rows = []
    for row in response:
        campaign = row.campaign
        metrics = row.metrics
        rows.append({
            "platform": "GoogleAds",
            "campaign_id": campaign.id,
            "name": campaign.name,
            "clicks": metrics.clicks,
            "impressions": metrics.impressions,
            "cpc": metrics.average_cpc.micros / 1e6,
            "cost": metrics.cost_micros / 1e6,
            "conversions": metrics.conversions,
        })
    return rows
