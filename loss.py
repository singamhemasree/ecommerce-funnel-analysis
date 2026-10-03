import duckdb

FILE = "data/2019-Dec.csv"

query = f"""
WITH users AS (
    SELECT
        COUNT(DISTINCT CASE WHEN event_type='view' THEN user_id END) AS viewed,
        COUNT(DISTINCT CASE WHEN event_type='cart' THEN user_id END) AS carted,
        COUNT(DISTINCT CASE WHEN event_type='purchase' THEN user_id END) AS purchased
    FROM read_csv_auto('{FILE}')
),
orders AS (
    SELECT AVG(price) AS avg_price
    FROM read_csv_auto('{FILE}')
    WHERE event_type = 'purchase'
)
SELECT
    ROUND(avg_price, 2) AS avg_item_price,
    viewed - carted AS lost_before_cart,
    carted - purchased AS lost_at_cart,
    ROUND((carted - purchased) * avg_price, 0) AS revenue_lost_at_cart
FROM users, orders
"""

print(duckdb.sql(query).df().T)