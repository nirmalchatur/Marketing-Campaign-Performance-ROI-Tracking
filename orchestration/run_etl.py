import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from etl.extract.load_sample_csv import load_sample_data
from etl.transform.transform_data import transform_campaign_data
from etl.load.load_to_db import load_to_mongo

if __name__ == "__main__":
    raw_df = load_sample_data()
    transformed_df = transform_campaign_data(raw_df)
    load_to_mongo(transformed_df)
