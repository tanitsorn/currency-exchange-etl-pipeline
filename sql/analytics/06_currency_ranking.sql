SELECT rate_date,
       target_currency AS currency,
       exchange_rate,
       ROW_NUMBER()OVER( 
        PARTITION BY rate_date
        ORDER BY exchange_rate DESC) AS currency_rank,
        CASE
            WHEN ROW_NUMBER() OVER(
                PARTITION BY rate_date
                ORDER BY exchange_rate DESC
            ) = 1
            THEN 'Strongest'

            WHEN ROW_NUMBER() OVER(
                PARTITION BY rate_date
                ORDER BY exchange_rate ASC
            ) = 1
            THEN 'Weakest'

            ELSE 'Normal'
        END AS strength_level
FROM exchange_rates
ORDER BY rate_date, currency_rank;
