-- =====================================================
-- File: 05_currency_volatility.sql
-- Description:
-- Measure exchange rate volatility for each currency
-- using the standard deviation of exchange rates.
-- =====================================================

SELECT
    target_currency,
    ROUND(STDDEV(exchange_rate), 6) AS currency_volatility
FROM exchange_rates
GROUP BY target_currency
ORDER BY currency_volatility DESC;