import pandas as pd
import io
from pymongo import MongoClient
import os
from datetime import datetime

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["marketing_tracker"]
collection = db["campaign_metrics"]

def get_all_campaigns(query=None):
    """
    Retrieve campaign metrics from MongoDB with optional query filter
    """
    if query is None:
        query = {}
    return list(collection.find(query))

def detect_anomalies(data, threshold=10):
    """
    Detect campaigns with ROI below threshold
    """
    anomalies = []
    for row in data:
        roi = row.get("ROI (%)", 0)
        try:
            if isinstance(roi, dict):
                continue  # skip if ROI is invalid
            if float(roi) < threshold:
                anomalies.append(row)
        except (ValueError, TypeError):
            continue
    return anomalies

def insert_csv_to_mongo(file_storage):
    """
    Insert CSV data into MongoDB
    """
    stream = io.StringIO(file_storage.stream.read().decode("UTF8"), newline=None)
    df = pd.read_csv(stream)

    # Convert date strings to datetime objects if needed
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

    # ✅ Calculate ROI if cost > 0
    if {'conversions', 'cost'}.issubset(df.columns):
        df["ROI (%)"] = ((df["conversions"] * 50 - df["cost"]) / df["cost"]) * 100
    else:
        df["ROI (%)"] = 0

    # Insert to MongoDB
    collection.insert_many(df.to_dict(orient="records"))

def prepare_chart_data(campaigns):
    """
    Prepare data for visualization charts
    """
    if not campaigns:
        return {"labels": [], "costs": [], "rois": []}
    
    data = pd.DataFrame(campaigns)
    
    # Ensure we have required columns
    labels = data.get("name", pd.Series(["Unknown"] * len(data))).tolist()
    costs = data.get("cost", pd.Series([0] * len(data))).tolist()
    rois = data.get("ROI (%)", pd.Series([0] * len(data))).tolist()
    
    return {
        "labels": labels,
        "costs": costs,
        "rois": rois
    }