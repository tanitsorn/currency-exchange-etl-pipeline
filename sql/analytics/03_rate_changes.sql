-- =====================================================
-- File: 03_rate_changes.sql
-- Description:
-- Calculate day-to-day exchange rate changes and
-- percentage changes using the LAG window function.
-- =====================================================

WITH previous_rates as (
    SELECT rate_date,
           target_currency,
           exchange_rate,
           LAG(exchange_rate) OVER(
                PARTITION BY target_currency
                ORDER BY rate_date
           ) AS previous_rate
    FROM exchange_rates
)

SELECT rate_date, 
       target_currency as currency,
       exchange_rate as rate,
       previous_rate,
       ROUND(exchange_rate - previous_rate, 5) AS rate_change,
       ROUND((exchange_rate - previous_rate)
              / previous_rate *100
              , 4) AS pct_change
FROM previous_rates
order by target_currency, rate_date;