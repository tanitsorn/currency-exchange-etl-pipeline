-- =====================================================
-- File: 06_currency_ranking.sql
-- Description:
-- Rank currencies by exchange rate for each day using
-- SQL window functions and classify them as
-- Strongest, Weakest, or Normal.
-- =====================================================

WITH ranking AS (
    SELECT rate_date,
           target_currency,
           exchange_rate,
           ROW_NUMBER() OVER(
            PARTITION BY rate_date
            ORDER BY exchange_rate DESC
           ) AS strongest_rank,
           ROW_NUMBER() OVER(
            PARTITION BY rate_date
            ORDER BY exchange_rate ASC 
           ) AS weakest_rank
    FROM exchange_rates
)

SELECT rate_date,
       target_currency AS currency,
       exchange_rate,
       strongest_rank,
       CASE
            WHEN strongest_rank = 1 THEN 'Strongest'
            WHEN weakest_rank = 1 THEN 'Weakest'
            ELSE 'Normal'
            END AS strength_level
FROM ranking
ORDER BY rate_date, strongest_rank;