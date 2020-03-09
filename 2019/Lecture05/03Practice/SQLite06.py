import sqlite3
 
# Connect to SQLite DB
conn = sqlite3.connect("test.db")

with conn:
    # Create Cursor from connection object
    cur = conn.cursor()
    cur.execute("DELETE FROM customer WHERE region = 'Daejeon'")
    cur.execute("INSERT INTO customer(name, category, region) values ('cbchoi', 1, 'Daejeon')")
    
    cur.execute('select* from customer')
    [print(row) for row in cur.fetchall()]
    
    conn.commit()
