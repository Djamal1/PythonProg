import sqlite3

conn = sqlite3.connect("cs_gamers.db")
bd_cur = conn.cursor()

bd_cur.execute("SELECT * FROM cs_gamers")
info = bd_cur.fetchall()
print(info)

bd_cur.close()
conn.close()