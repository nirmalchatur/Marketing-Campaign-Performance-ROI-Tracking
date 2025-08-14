from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import pandas as pd
from io import StringIO
import requests
from bs4 import BeautifulSoup

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "your-secret-key-here")

# MongoDB connection
def get_db():
    client = MongoClient(os.getenv("MONGO_URI"))
    return client.get_database("marketing_tracker")

# ---------------------- Dashboard & Anomalies ----------------------

@app.route("/")
def index():
    db = get_db()
    start_date = request.args.get("start")
    end_date = request.args.get("end")

    query = {}
    if start_date and end_date:
        query["date"] = {"$gte": start_date, "$lte": end_date}

    campaigns = list(db.campaign_metrics.find(query))
    anomalies = [c for c in campaigns if c.get("ROI (%)", 100) < 10]
    
    chart_data = {
        "labels": [c.get("campaign_name", "Unknown") for c in campaigns],
        "costs": [c.get("cost", 0) for c in campaigns],
        "rois": [c.get("ROI (%)", 0) for c in campaigns]
    }

    return render_template("index.html", 
                         anomalies=anomalies, 
                         chart_data=chart_data,
                         request=request)

@app.route("/clear_anomalies", methods=["POST"])
def clear_anomalies():
    try:
        db = get_db()
        result = db.campaign_metrics.delete_many({"ROI (%)": {"$lt": 10}})
        flash(f"✅ Cleared {result.deleted_count} anomalies!", "success")
    except Exception as e:
        flash(f"❌ Error clearing anomalies: {str(e)}", "error")
    return redirect(url_for("index"))

@app.route("/clear_database", methods=["POST"])
def clear_database():
    try:
        db = get_db()
        result = db.campaign_metrics.delete_many({})
        flash(f"✅ Cleared entire database ({result.deleted_count} records)", "success")
    except Exception as e:
        flash(f"❌ Error clearing database: {str(e)}", "error")
    return redirect(url_for("index"))

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        db = get_db()
        file = request.files["file"]
        if file and file.filename.endswith(".csv"):
            try:
                stream = StringIO(file.stream.read().decode("UTF8"))
                df = pd.read_csv(stream)
                
                if 'date' in df.columns:
                    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
                
                records = df.to_dict('records')
                db.campaign_metrics.insert_many(records)
                flash(f"✅ Uploaded {len(records)} records!", "success")
            except Exception as e:
                flash(f"❌ Upload error: {str(e)}", "error")
            return redirect(url_for("index"))
        else:
            flash("❌ Please upload a valid CSV file", "error")
    return render_template("upload.html")

# ---------------------- Web Scraper ----------------------

@app.route("/scrape", methods=["GET", "POST"])
def scrape():
    if request.method == "POST":
        url = request.form.get("url")
        if not url:
            flash("❌ Please provide a URL", "error")
            return redirect(url_for("scrape"))

        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            resp = requests.get(url, headers=headers, timeout=10)
            resp.raise_for_status()

            soup = BeautifulSoup(resp.text, "html.parser")
            headlines = [h.get_text(strip=True) for h in soup.find_all("h2")]

            return render_template("scraper.html", results=headlines)
        except Exception as e:
            flash(f"❌ Scraping error: {str(e)}", "error")
            return redirect(url_for("scrape"))

    return render_template("scraper.html", results=None)

# ---------------------- Startup ----------------------

if __name__ == "__main__":
    try:
        db = get_db()
        db.command('ping')
        print("✅ Successfully connected to MongoDB!")
    except Exception as e:
        print("❌ MongoDB connection error:", e)
    app.run(debug=True)
