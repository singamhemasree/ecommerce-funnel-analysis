import duckdb

con = duckdb.connect()
con.execute("""
COPY (SELECT * FROM read_csv_auto('data/2019-Oct.csv'))
TO 'data/oct.parquet' (FORMAT PARQUET);
""")
print("done")