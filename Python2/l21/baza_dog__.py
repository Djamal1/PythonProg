import sqlite3

conn = sqlite3.connect("list_of_dog.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS list_of_dog(
	id INT PRIMARY KEY,
	name VARCHAR(24),
	force VARCHAR(10),
	friendliness VARCHAR(10),
	speed REAL
)""")

cur.execute("INSERT INTO list_of_dog VALUES(1, 'Бультерьер',8,9,7)")
cur.execute("INSERT INTO list_of_dog VALUES(2, 'Акита',8,5,6)")
cur.execute("INSERT INTO list_of_dog VALUES(3, 'Аффенпинчер',1,10,4)")
cur.execute("INSERT INTO list_of_dog VALUES(4, 'Басенджи',2,10,8)")
cur.execute("INSERT INTO list_of_dog VALUES(5, 'Бигль',3,10,5)")
cur.execute("INSERT INTO list_of_dog VALUES(6, 'Босерон',7,10,8)")


conn.commit()

cur.close()
conn.close()