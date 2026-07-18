-- =====================================================
-- File: 02_daily_summary.sql
-- Description:
-- Generate daily exchange rate statistics including
-- average, minimum, maximum, and daily spread.
-- =====================================================

SELECT rate_date,
       COUNT(*) AS total_currencies,
       ROUND(AVG(exchange_rate) ,5) AS average_rate,
       MIN(exchange_rate) AS lowest_rate,
       MAX(exchange_rate) AS highest_rate,
       ROUND(
        MAX(exchange_rate) - MIN(exchange_rate)
        , 5) AS daily_spread
FROM exchange_rates
GROUP BY rate_date
ORDER BY rate_date;