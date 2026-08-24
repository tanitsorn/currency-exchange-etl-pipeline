import pandas as pd

from python.validation.validation_exchange_rates import (
    validate_exchange_rates,
)


def test_validation_passes_for_valid_data():
    df = pd.DataFrame({
        "rate_date": ["2026-08-21", "2026-08-21"],
        "base_currency": ["USD", "USD"],
        "target_currency": ["THB", "EUR"],
        "exchange_rate": [32.675, 0.85477],
    })

    result = validate_exchange_rates(df)

    assert result["missing_values"] == 0
    assert result["duplicate_rows"] == 0
    assert result["invalid_rates"] == 0


def test_validation_detects_missing_values():
    df = pd.DataFrame({
        "rate_date": ["2026-08-21"],
        "base_currency": ["USD"],
        "target_currency": ["THB"],
        "exchange_rate": [None],
    })

    result = validate_exchange_rates(df)

    assert result["missing_values"] == 1


def test_validation_detects_invalid_rates():
    df = pd.DataFrame({
        "rate_date": ["2026-08-21"],
        "base_currency": ["USD"],
        "target_currency": ["THB"],
        "exchange_rate": [-10],
    })

    result = validate_exchange_rates(df)

    assert result["invalid_rates"] == 1