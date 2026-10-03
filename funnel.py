import duckdb

FILE = "data/2019-Dec.csv"

query = f"""
WITH steps AS (
    SELECT
        COUNT(DISTINCT CASE WHEN event_type='view' THEN user_id END) AS viewed,
        COUNT(DISTINCT CASE WHEN event_type='cart' THEN user_id END) AS carted,
        COUNT(DISTINCT CASE WHEN event_type='purchase' THEN user_id END) AS purchased
    FROM read_csv_auto('{FILE}')
)
SELECT
    viewed, carted, purchased,
    ROUND(100.0 * carted / viewed, 1) AS view_to_cart_pct,
    ROUND(100.0 * purchased / carted, 1) AS cart_to_purchase_pct,
    ROUND(100.0 * purchased / viewed, 1) AS overall_pct
FROM steps
"""

print(duckdb.sql(query).df().T)