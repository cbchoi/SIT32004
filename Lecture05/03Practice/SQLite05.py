import sqlite3
 
# Connect to SQLite DB
conn = sqlite3.connect("test.db")

with conn:
    # Create Cursor from connection object
    cur = conn.cursor()
    #sql = "insert into customer (name,category, region) values (?,?,?)"
    infoList = [('t.choi', 1, 'Seoul'), ('J.Kim', 2, 'Busan'), ('M.Lee', 2, 'Daejeon')]
    #cur.executemany(sql,infoList)

    cur.execute('select* from customer')
    [print(row) for row in cur.fetchall()]
    
    conn.commit()
