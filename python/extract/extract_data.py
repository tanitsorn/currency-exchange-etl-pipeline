import json
import os
from datetime import datetime
import requests

API_URL = (
    "https://api.frankfurter.app/latest"
    "?from=USD"
    "&to=THB,EUR,JPY,GBP,AUD,CAD,CHF,CNY"
)

def fetch_exchange_rates():
    """Fetch latest exchange rates from Frankfurter API."""
    
    response = requests.get(API_URL, timeout=10)

    response.raise_for_status()

    return response.json()

def save_raw_json(data):
    """Save raw API response to data/raw/ as a JSON file."""

    os.makedirs("data/raw", exist_ok=True)

    today = datetime.today().strftime("%Y-%m-%d")

    file_path = f"data/raw/exchange_rate_{today}.json"
    
    print(f"Saving to: {file_path}")

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return file_path