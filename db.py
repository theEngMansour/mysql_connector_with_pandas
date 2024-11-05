import mysql.connector
import pandas as pd

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tesssss"
)

df = pd.read_csv("إقليم عدن.csv")
cursor = conn.cursor()

for index, row in df.iterrows():
    cursor.execute('''
          INSERT INTO tabs (name, slug)
          VALUES (%s, %s)
      ''', ('wq', row['title']))


conn.commit()
cursor.close()
conn.close()