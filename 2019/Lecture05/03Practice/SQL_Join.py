import sqlite3

def create_tbl(conn):
	conn.execute("CREATE TABLE StuName(id integer primary key, fname text not null, lname text not null)")
	conn.execute("CREATE TABLE Grade(id integer primary key, grade text not null)")
	conn.execute("CREATE TABLE Department(id integer primary key, dept text not null)") 

def insert_to_tbl(conn):
	conn.execute("INSERT INTO StuName(id, fname, lname) VALUES (2110001, 'Smith', 'John')")
	conn.execute("INSERT INTO StuName(id, fname, lname) VALUES (2110002, 'Choi', 'Thea')")
	conn.execute("INSERT INTO StuName(id, fname, lname) VALUES (2110003, 'Kim', 'Nana')")

	conn.execute("INSERT INTO Grade(id, grade) VALUES (2110001, 'A+')")
	conn.execute("INSERT INTO Grade(id, grade) VALUES (2110002, 'A+')")
	conn.execute("INSERT INTO Grade(id, grade) VALUES (2110003, 'B+')")

	conn.execute("INSERT INTO Department(id, dept) VALUES (2110001, 'EECS')")
	conn.execute("INSERT INTO Department(id, dept) VALUES (2110002, 'GEICT')")	
	conn.execute("INSERT INTO Department(id, dept) VALUES (2110003, 'ME')")		

# Connect to SQLite DB
conn = sqlite3.connect("join.db")

with conn:
    # Create Cursor from connection object
    cur = conn.cursor()
     
    # SQL Query
    create_tbl(conn)
    insert_to_tbl(conn)

    cur.execute("SELECT * from StuName, Grade, Department WHERE StuName.id = Grade.id AND Grade.id = Department.id;")

    for row in cur.fetchall():
    	print(row)

    conn.commit()
