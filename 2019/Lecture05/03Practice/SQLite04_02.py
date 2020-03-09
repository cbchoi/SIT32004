import sqlite3
 
# Connect to SQLite DB
conn = sqlite3.connect("test.db")

with conn:
    # Create Cursor from connection object
    cur = conn.cursor()
     
    # SQL Query
    cur.execute("SELECT name from customer WHERE category = 1;")

    for row in cur.fetchall():
    	print(row)
    
    conn.commit()
