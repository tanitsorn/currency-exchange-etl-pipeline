CREATE DATABASE IF NOT EXISTS currency_exchange;

USE currency_exchange;

CREATE TABLE IF NOT EXISTS exchange_rates (
    rate_date DATE NOT NULL,
    base_currency CHAR(3) NOT NULL,
    target_currency CHAR(3) NOT NULL,
    exchange_rate DECIMAL(10,5) NOT NULL,

    PRIMARY KEY (rate_date, base_currency, target_currency)
);