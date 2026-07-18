-- =====================================================
-- File: 04_cross_currency.sql
-- Description:
-- Calculate cross-currency exchange rates between
-- currencies using USD as the common base currency.
-- =====================================================

SELECT a.rate_date,
       a.exchange_rate AS usd_to_thb,
       b.exchange_rate AS usd_to_eur,
       ROUND(b.exchange_rate /
             a.exchange_rate
             , 6) AS thb_to_eur
FROM exchange_rates a 
JOIN exchange_rates b 
ON a.rate_date = b.rate_date
WHERE a.target_currency='THB' 
AND b.target_currency='EUR'
ORDER BY a.rate_date;