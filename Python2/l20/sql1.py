import sqlite3

conn = sqlite3.connect("cs_gamers.db")
bd_cur = conn.cursor()

# bd_cur.execute("DROP TABLE cs_gamers")

bd_cur.execute("""CREATE TABLE cs_gamers (
	name VARCHAR(16) PRIMARY KEY,
	rating VARCHAR(10),
	stats REAL,
	top_gun VARCHAR(30)
)""")

bd_cur.execute("INSERT INTO cs_gamers VALUES('кто_то', 'Глобал', 1.8, 'Керамбит Крововая паутина')")
bd_cur.execute("INSERT INTO cs_gamers VALUES('кто', 'Беркут 2', 1.6, 'Драгонлор')")

# bd_cur.execute("INSERT INTO cs_gamers VALUES(?, ?, ?, ?)", ("Султанмурад", "Сильвер 1", 1.5, "QBZ95"))
ins = "INSERT INTO cs_gamers VALUES(?, ?, ?, ?)"
data = "Султанмурад", "Сильвер 1", 1.5, "QBZ95"
bd_cur.execute(ins, data)

conn.commit()

bd_cur.close()
conn.close()