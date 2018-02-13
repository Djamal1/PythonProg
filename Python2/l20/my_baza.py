import sqlite3

conn = sqlite3.connect("cats.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE cats (
	name VARCHAR(24) PRIMARY KEY,
	force VARCHAR(10),
	beauty VARCHAR(5),
	adroitness REAL
)""")

cur.execute("INSERT INTO cats VALUES('Британец', 4, 3, 3)")
cur.execute("INSERT INTO cats VALUES('Русская голубая', 7, 4, 7)")
cur.execute("INSERT INTO cats VALUES('Сибирская', 8, 3, 6)")
cur.execute("INSERT INTO cats VALUES('Шотланская', 5, 5, 6)")

conn.commit()

cur.close()
conn.close()