import sqlite3

conn = sqlite3.connect("list_of_worker.db")
cur = conn.cursor()
# cur.execute("DROP TABLE list_of_worker")

cur.execute("""CREATE TABLE IF NOT EXISTS list_of_worker(
	surname VARCHAR(30),
	name VARCHAR(24),
	post VARCHAR(20),
	record REAL
)""")

cur.execute("INSERT INTO list_of_worker VALUES('names', 'name', 'LOLOLOLOLO', 10)")
cur.execute("INSERT INTO list_of_worker VALUES('kekekee', 'kek', 'LOgLO', 3)")
cur.execute("INSERT INTO list_of_worker VALUES('noooo', 'nameee', 'LOL', 4)")
cur.execute("INSERT INTO list_of_worker VALUES('no', 'noo', 'LO', 6)")
cur.execute("INSERT INTO list_of_worker VALUES('kkee', 'kke', 'LOllll', 8)")
cur.execute("INSERT INTO list_of_worker VALUES('nffd', 'ndzddf', 'LdjjfO', 9)")


conn.commit()

cur.close()
conn.close()