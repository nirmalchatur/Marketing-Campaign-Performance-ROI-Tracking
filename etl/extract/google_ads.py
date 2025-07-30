from google.ads.googleads.client import GoogleAdsClient
import os

def fetch_google_ads_data():
    client = GoogleAdsClient.load_from_storage("config/google-ads.yaml")
    ga_service = client.get_service("GoogleAdsService")

    query = """
        SELECT campaign.id, campaign.name, metrics.clicks, metrics.impressions,
               metrics.average_cpc, metrics.cost_micros, metrics.conversions
        FROM campaign
        WHERE segments.date DURING LAST_7_DAYS
    """
    response = ga_service.search(customer_id="YOUR_CUSTOMER_ID", query=query)
    
    data = []
    for row in response:
        data.append({
            "platform": "GoogleAds",
            "campaign_id": row.campaign.id,
            "name": row.campaign.name,
            "clicks": row.metrics.clicks,
            "impressions": row.metrics.impressions,
            "cost": row.metrics.cost_micros / 1e6,
            "conversions": row.metrics.conversions,
        })
    return pd.DataFrame(data)
