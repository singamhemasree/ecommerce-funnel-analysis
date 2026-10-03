import duckdb

FILE = "data/2019-Dec.csv"

query = f"""
SELECT
    COALESCE(split_part(category_code, '.', 1), 'unknown') AS category,
    COUNT(DISTINCT CASE WHEN event_type='view' THEN user_id END) AS viewed,
    COUNT(DISTINCT CASE WHEN event_type='cart' THEN user_id END) AS carted,
    COUNT(DISTINCT CASE WHEN event_type='purchase' THEN user_id END) AS purchased,
    ROUND(100.0 * COUNT(DISTINCT CASE WHEN event_type='purchase' THEN user_id END)
          / NULLIF(COUNT(DISTINCT CASE WHEN event_type='cart' THEN user_id END), 0), 1)
          AS cart_to_purchase_pct
FROM read_csv_auto('{FILE}')
GROUP BY 1
ORDER BY viewed DESC
"""

print(duckdb.sql(query).df().to_string())