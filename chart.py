import duckdb
import plotly.graph_objects as go

FILE = "data/2019-Dec.csv"

df = duckdb.sql(f"""
SELECT
    COUNT(DISTINCT CASE WHEN event_type='view' THEN user_id END) AS viewed,
    COUNT(DISTINCT CASE WHEN event_type='cart' THEN user_id END) AS carted,
    COUNT(DISTINCT CASE WHEN event_type='purchase' THEN user_id END) AS purchased
FROM read_csv_auto('{FILE}')
""").df()

steps = ["Viewed", "Added to cart", "Purchased"]
values = df.iloc[0].tolist()

fig = go.Figure(go.Funnel(y=steps, x=values, textinfo="value+percent previous"))
fig.update_layout(title="Shopper funnel, December 2019")
fig.write_html("funnel.html")
print("saved funnel.html")