import pandas as pd
import psycopg2 as pg

host = "localhost"
db = "test"
user = "test"
password = "test"

table = "mytable"

connection = pg.connect(f"host={host} dbname={db} user={user} password={password}")
df = pd.read_sql_query('SELECT * FROM {table}', connection)

columns = df.columns
print(f"Columns: {columns}")

for index, row in df.iterrows():
    print(row['id'])
