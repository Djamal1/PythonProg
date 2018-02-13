import sqlite3

conn = sqlite3.connect("cats.db")
cur = conn.cursor()

cur.execute("SELECT * FROM cats")
info = cur.fetchall()
print(info)

cur.close()
conn.close()