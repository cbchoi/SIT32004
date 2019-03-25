import sqlite3
 
# Connect to SQLite DB
conn = sqlite3.connect("store.db")

with conn:
    # Create Cursor from connection object
	cur = conn.cursor()
	#cur.execute("CREATE TABLE stock(name text not null, quanity integer, price integer);")
	#cur.execute("INSERT INTO stock(name, quanity, price) VALUES ('apple',889,190);")
	#cur.execute("INSERT INTO stock(name, quanity, price) VALUES ('carrot',600,60);")
    
	cur.execute("SELECT * FROM stock") 
	#for result in cur.fetchall():
	#	print(result)
	[print(result) for result in cur.fetchall()]
    # Reflect to Database
	conn.commit()

conn.close()