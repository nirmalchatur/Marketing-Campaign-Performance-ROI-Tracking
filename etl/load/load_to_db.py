from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def get_mongo_client():
    uri = os.getenv("MONGO_URI")
    return MongoClient(uri)

def load_to_mongo(df: pd.DataFrame):
    client = get_mongo_client()
    db_name = os.getenv("MONGO_DB", "marketing_db")
    coll_name = os.getenv("MONGO_COLLECTION", "campaign_metrics")

    db = client[db_name]
    collection = db[coll_name]

    # Optional: Drop existing collection to avoid duplicates
    collection.drop()

    # Insert documents (convert DataFrame to dict)
    collection.insert_many(df.to_dict(orient="records"))

    print(f"✅ Data loaded into MongoDB collection: {coll_name}")
    client.close()
