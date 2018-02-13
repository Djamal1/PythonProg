import sqlite3

conn = sqlite3.connect("list_of_dog.db")
cur = conn.cursor()

cur.execute("SELECT * FROM list_of_dog")

info = cur.fetchall()
print(info)

cur.close()
conn.close()