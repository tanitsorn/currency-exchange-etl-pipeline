-- =====================================================
-- File: 01_currency_strength.sql
-- Description:
-- Calculate average, minimum, and maximum exchange rates
-- for each currency across all available dates.
-- =====================================================

SELECT target_currency,
       COUNT(*) AS total_days,
       ROUND(AVG(exchange_rate) ,5) AS average_rate,
       MIN(exchange_rate) AS lowest_rate,
       MAX(exchange_rate) AS highest_rate
FROM exchange_rates
GROUP BY target_currency
ORDER BY average_rate DESC;