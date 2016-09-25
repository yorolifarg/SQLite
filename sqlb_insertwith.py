import sqlite3
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO population VALUES ('West Worthing','WW',87000)")
    
    c.close()

print("All data has been inserted")