import sqlite3
 
# Connect to SQLite DB
con = sqlite3.connect("retak2e.db")

with con:
    # Create Cursor from connection object
    cur = con.cursor()
     
    # Put SQL Query
    #cur.execute("CREATE TABLE customer(id integer primary key autoincrement, name text not null, category integer, region text);")

    #cur.execute("INSERT INTO customer(name, category, region) values ('cbchoi', 1, 'Daejeon');")
    #cur.execute("SELECT * FROM customer;")

    #for item in cur.fetchall():
    #	print(item)
    
    #cur.execute("INSERT INTO customer(name, category, region) values ('cbchoi2', 12, 'Pohang');")

    #sql = "insert into customer (name, category, region) values (?, ?, ?)"
    infoList = [('r.choi', 1, 'Seoul'), ('H.Kim', 2, 'Busan'), ('N.Lee', 2, 'Daejeon')]
    #cur.executemany(sql, infoList)

    cur.execute("SELECT * FROM customer")
    [print(item) for item in cur.fetchall()]

    for item in infoList:
    	cur.execute(f"insert into customer (name, category, region) values ('{item[0]}', {item[1]}, '{item[2]}')")

    cur.execute("SELECT * FROM customer")
    [print(item) for item in cur.fetchall()]

    #print("before deletion")    	
    #cur.execute("DELETE FROM customer WHERE *;")
    
    #cur.execute("SELECT * FROM customer")
    #[print(item) for item in cur.fetchall()]
    # Reflect to Database
    con.commit()
