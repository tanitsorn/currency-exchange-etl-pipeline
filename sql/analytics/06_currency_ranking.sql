-- =====================================================
-- File: 06_currency_ranking.sql
-- Description:
-- Rank currencies by exchange rate for each day using
-- SQL window functions and classify them as
-- Highest Rate, Lowest Rate, or Normal.
-- =====================================================

WITH ranking AS (
    SELECT
        rate_date,
        target_currency,
        exchange_rate,
        ROW_NUMBER() OVER(
            PARTITION BY rate_date
            ORDER BY exchange_rate DESC
        ) AS highest_rate_rank,
        ROW_NUMBER() OVER(
            PARTITION BY rate_date
            ORDER BY exchange_rate ASC
        ) AS lowest_rate_rank
    FROM exchange_rates
)

SELECT
    rate_date,
    target_currency AS currency,
    exchange_rate,
    highest_rate_rank,
    CASE
        WHEN highest_rate_rank = 1 THEN 'Highest Rate'
        WHEN lowest_rate_rank = 1 THEN 'Lowest Rate'
        ELSE 'Normal'
    END AS rate_level
FROM ranking
ORDER BY rate_date, highest_rate_rank;