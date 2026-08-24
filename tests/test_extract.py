from unittest.mock import Mock, patch

from python.extract.extract_data import fetch_exchange_rates


@patch("python.extract.extract_data.requests.get")
def test_fetch_exchange_rates(mock_get):
    mock_response = Mock()

    mock_response.json.return_value = {
        "amount": 1,
        "base": "USD",
        "date": "2026-08-21",
        "rates": {
            "THB": 32.675,
            "EUR": 0.85477,
            "JPY": 158.70,
        },
    }

    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = fetch_exchange_rates("2026-08-21")

    assert result["base"] == "USD"
    assert result["date"] == "2026-08-21"
    assert result["rates"]["THB"] == 32.675
    assert result["rates"]["EUR"] == 0.85477

    mock_get.assert_called_once()