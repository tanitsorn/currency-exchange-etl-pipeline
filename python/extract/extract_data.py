import json
import os
from datetime import datetime
import requests

def fetch_exchange_rates(date=None):
    """Fetch latest exchange rates from Frankfurter API."""

    if date is None:
        url = (
            "https://api.frankfurter.app/latest"
            "?from=USD"
            "&to=THB,EUR,JPY,GBP,AUD,CAD,CHF,CNY"
        )
    else:
        url = (
            f"https://api.frankfurter.app/{date}"
            "?from=USD"
            "&to=THB,EUR,JPY,GBP,AUD,CAD,CHF,CNY"
        )
    
    response = requests.get(url, timeout=10)

    response.raise_for_status()

    return response.json()

def save_raw_json(data, target_date=None):
    """Save raw API response to data/raw/ as a JSON file."""

    os.makedirs("data/raw", exist_ok=True)

    if target_date is None:
        file_date = datetime.today().strftime("%Y-%m-%d")
    else:
        file_date = target_date
    file_path = f"data/raw/exchange_rate_{file_date}.json"
    
    print(f"Saving to: {file_path}")

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return file_path