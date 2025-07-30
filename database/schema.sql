CREATE TABLE IF NOT EXISTS campaign_metrics (
    id SERIAL PRIMARY KEY,
    campaign_id VARCHAR(100),
    platform VARCHAR(50),
    impressions INT,
    clicks INT,
    cost FLOAT,
    conversions INT,
    roi FLOAT,
    date DATE
);
