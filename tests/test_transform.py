import json

from python.transform.transform_exchange_rates import (
    transform_exchange_rates,
)


def test_transform_exchange_rates(tmp_path):
    data = {
        "amount": 1,
        "base": "USD",
        "date": "2026-08-21",
        "rates": {
            "THB": 32.675,
            "EUR": 0.85477,
        },
    }

    json_path = tmp_path / "exchange_rate.json"

    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(data, file)

    df, output_path = transform_exchange_rates(
        str(json_path)
    )

    assert len(df) == 2
    assert set(df["target_currency"]) == {"THB", "EUR"}
    assert set(df["base_currency"]) == {"USD"}
    assert output_path.endswith(
        "exchange_rates_2026-08-21.csv"
    )