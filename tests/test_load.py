from unittest.mock import MagicMock

from python.load.load_to_mysql import rate_exists


def test_rate_exists_returns_true_when_data_exists():
    engine = MagicMock()
    connection = engine.connect.return_value.__enter__.return_value

    result = MagicMock()
    result.scalar.return_value = 8

    connection.execute.return_value = result

    assert rate_exists(engine, "2026-08-21") is True


def test_rate_exists_returns_false_when_data_does_not_exist():
    engine = MagicMock()
    connection = engine.connect.return_value.__enter__.return_value

    result = MagicMock()
    result.scalar.return_value = 0

    connection.execute.return_value = result

    assert rate_exists(engine, "2026-08-24") is False