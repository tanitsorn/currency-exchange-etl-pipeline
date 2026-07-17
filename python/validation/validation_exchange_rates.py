def validate_exchange_rates(df):
    """Validation transformed exchange rate data."""

    # Missing values
    missing_values = df.isnull().sum().sum()

    # Duplicate rows
    duplicate_rows = df.duplicated().sum()

    # Invalid exchange rates
    invalid_rates = (df["exchange_rate"] <= 0).sum()

    return {
        "missing_values": missing_values,
        "duplicate_rows": duplicate_rows,
        "invalid_rates": invalid_rates,
    }