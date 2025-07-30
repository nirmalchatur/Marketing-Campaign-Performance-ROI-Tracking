# Marketing Campaign Performance & ROI Tracker

Track and analyze cross-platform marketing campaign performance, calculate ROI, and detect anomalies.

## Features
- Data ingestion from Google Ads, Facebook Ads, Mailchimp
- ROI & KPI normalization
- PostgreSQL/BigQuery backend
- Metabase dashboard integration
- Slack/email-based anomaly alerts

## Setup Instructions
1. Create `.env` from `config.env.example` and add API tokens
2. Install dependencies: `pip install -r requirements.txt`
3. Run DB schema: `psql -U postgres -d marketing_db -f database/schema.sql`
4. Execute pipeline: `python orchestration/daily_pipeline.py`
