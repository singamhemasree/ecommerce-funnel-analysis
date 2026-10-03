import duckdb

FILE = "data/2019-Dec.csv"

query = f"""
SELECT
    CASE
        WHEN price < 2 THEN '1. under 2'
        WHEN price < 5 THEN '2. 2 to 5'
        WHEN price < 10 THEN '3. 5 to 10'
        WHEN price < 50 THEN '4. 10 to 50'
        ELSE '5. 50 and above'
    END AS price_band,
    COUNT(DISTINCT CASE WHEN event_type='cart' THEN user_id END) AS carted,
    COUNT(DISTINCT CASE WHEN event_type='purchase' THEN user_id END) AS purchased,
    ROUND(100.0 * COUNT(DISTINCT CASE WHEN event_type='purchase' THEN user_id END)
          / NULLIF(COUNT(DISTINCT CASE WHEN event_type='cart' THEN user_id END), 0), 1)
          AS cart_to_purchase_pct
FROM read_csv_auto('{FILE}')
GROUP BY 1
ORDER BY 1
"""

print(duckdb.sql(query).df().to_string())