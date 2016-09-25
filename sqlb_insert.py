#import sqlite3 library
import sqlite3

#create connection object
conn = sqlite3.connect("new.db")

#get a cursor to execute SQL commands
cursor = conn.cursor()

#insert data
cursor.execute("INSERT INTO population VALUES('Littlehampton','LIT',20000)")
cursor.execute("INSERT INTO population VALUES('Worthing','WOR',50000)")

#commit the changes
conn.commit()

#close the connection
conn.close()

print("All data has been inserted.")
