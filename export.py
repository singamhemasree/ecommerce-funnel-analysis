import duckdb

con = duckdb.connect()
f = "data/2019-Dec.csv"

funnel = con.execute(f"""
SELECT event_type, COUNT(DISTINCT user_id) AS users
FROM read_csv_auto('{f}')
WHERE event_type IN ('view','cart','purchase')
GROUP BY event_type
""").df()
funnel.to_csv("funnel_summary.csv", index=False)

bands = con.execute(f"""
SELECT
  CASE WHEN price < 5 THEN '1. Under 5'
       WHEN price < 10 THEN '2. 5-10'
       WHEN price < 20 THEN '3. 10-20'
       WHEN price < 50 THEN '4. 20-50'
       ELSE '5. 50+' END AS price_band,
  event_type,
  COUNT(DISTINCT user_id) AS users
FROM read_csv_auto('{f}')
WHERE event_type IN ('view','cart','purchase')
GROUP BY 1, 2
ORDER BY 1, 2
""").df()
bands.to_csv("price_band_summary.csv", index=False)

print("Done")