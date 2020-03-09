import sqlite3
 
# Connect to SQLite DB
conn = sqlite3.connect("test.db")

with conn:
    # Create Cursor from connection object
    cur = conn.cursor()
     
    # SQL Query

    conn.commit()
