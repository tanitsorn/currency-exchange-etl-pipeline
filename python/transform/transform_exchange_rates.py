import os

import pandas as pd


def transform_exchange_rates(json_path, target_date=None):
    """Transform raw exchange rate JSON into a tabular DataFrame."""

    df = pd.read_json(json_path)

    df = df.reset_index()

    df = df.rename(
        columns={
            "index": "target_currency",
            "base": "base_currency",
            "date": "rate_date",
            "rates": "exchange_rate",
        }
    )

    df = df.drop(columns=["amount"])

    df = df.sort_values("target_currency")

    os.makedirs("data/clean", exist_ok=True)

    file_date = df["rate_date"].iloc[0].strftime("%Y-%m-%d")

    output_path = f"data/clean/exchange_rates_{file_date}.csv"

    df.to_csv(output_path, index=False)

    return df, output_path