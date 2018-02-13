import sqlite3

conn = sqlite3.connect("list_of_worker.db")
cur = conn.cursor()

cur.execute("SELECT DISTINCT record FROM list_of_worker")

info = cur.fetchall()
print(info)

cur.close()
conn.close()