import sys
import os

# Add the root directory to sys.path so we can import etl modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from etl.extract.load_sample_csv import load_sample_data

def test():
    df = load_sample_data()
    print(df.head())

if __name__ == "__main__":
    test()
