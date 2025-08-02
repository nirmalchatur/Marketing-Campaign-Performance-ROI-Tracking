# 📊 Marketing Campaign Performance & ROI Tracking

## 🧩 Overview
This project builds a real-time, multi-channel marketing performance tracking system using MongoDB, Python ETL, Metabase dashboards, and Slack alerting.

## 🎯 Objectives
- Automate data ingestion from ad platforms (sample simulated)
- Normalize and store metrics in MongoDB
- Create dynamic dashboards for KPIs (ROI, CTR, etc.)
- Send alerts via Slack when anomalies occur

---

## 🛠️ Tools Used
- Python, Pandas
- MongoDB Atlas (cloud)
- Metabase (Docker)
- Slack Webhook for Alerts

---

## 🧱 MongoDB Schema

```json
{
  "platform": "GoogleAds",
  "campaign_id": "GA123",
  "campaign_name": "Brand Awareness",
  "clicks": 120,
  "impressions": 3000,
  "cost": 150.0,
  "conversions": 10,
  "date": "2025-07-28"
}
