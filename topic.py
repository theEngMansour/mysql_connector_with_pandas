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
         INSERT INTO `topics`
         (`title`, 
         `content`, 
         `type`, 
         `file`, 
         `is_active`, 
         `tab_id`, 
         `user_id`, 
         `branch_id`, 
         `area_id`
         ) VALUES 
         (%s, %s, %s, %s, %s, %s, %s, %s, %s)''',
         (row['title'], row['content'], 'news', row['file'], True, 8, 1, 17, 1))

conn.commit()
cursor.close()
conn.close()
