import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")

# conn.execute('''CREATE TABLE COMPANY 
#         (ID INT PRIMARY KEY NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL);''')
# print("Table created successfully")

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE) \
#       VALUES (1, 'Paul', 32)")
# conn.commit()
# print ("Records created successfully")

cursor = conn.execute("SELECT id, name from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])

print("Operation done successfully")

conn.close()