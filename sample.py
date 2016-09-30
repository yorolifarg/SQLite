import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO cars VALUES('Mazda','Maz 323', 3)")
    
    c.close()
    
    print("All data has been inserted.")
    