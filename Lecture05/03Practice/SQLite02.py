import sqlite3
 
# Connect to SQLite DB
conn = sqlite3.connect("test.db")

with conn:
    # Create Cursor from connection object
    cur = conn.cursor()
     
    # SQL Query
    # Create Table
    cur.execute("CREATE TABLE customer(id integer primary key autoincrement, name text not null, category integer, region text);")
    
    conn.commit()
