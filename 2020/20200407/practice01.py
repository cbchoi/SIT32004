import sqlite3
 
# Connect to SQLite DB
conn = sqlite3.connect("test.db")

with conn:
    # Create Cursor from connection object
    cur = conn.cursor()
     
    # Put SQL Query
    #cur.execute("CREATE TABLE customer(id integer primary key autoincrement, name text not null, category integer, region text);")
    #cur.execute("INSERT INTO customer(name, category, region) values ('cbchoi', 2, 'Pohang');")
    #cur.execute("INSERT INTO customer(name, category, region) values ('jekim', 2, 'Pohang');")
    #cur.execute("SELECT name FROM customer WHERE region='Daejeon'")
    
    #for row in cur.fetchall():
    #	print(row)
    cur.execute('SELECT * FROM customer;')
    [print(row) for row in cur.fetchall()]

    cur.execute("DELETE FROM customer WHERE region = 'Daejeon'")

    #sql = "insert into customer (name,category, region) values (?,?,?);"
#    infoList = [('r.choi', 1, 'Seoul'), ('H.Kim', 2, 'Busan'), ('N.Lee', 2, 'Daejeon')]

    #cur.executemany(sql, infoList)
 #   for item in infoList:
    	#print(item[0], item[1], item[2])
    	#print(f"insert into customer (name,category, region) values ('{item[0]}', '{item[1]}', '{item[2]}');")
 #   	cur.execute(f"insert into customer (name,category, region) values ('{item[0]}', '{item[1]}', '{item[2]}');")

    cur.execute('SELECT * FROM customer;')
    [print(row) for row in cur.fetchall()]

    # Reflect to Database
    conn.commit()
