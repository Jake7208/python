#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('test_database.db')

cursor = connection.cursor()

# create table

command1 = """CREATE TABLE IF NOT EXISTS
test(id INTEGER PRIMARY KEY, FirstName TEXT, LastName TEXT, Address TEXT, City TEXT, State TEXT, zip TEXT, phoneNumber TEXT)
"""

cursor.execute(command1)

# add rows

cursor.execute("INSERT INTO test VALUES (1, 'Almira', 'Junior', '11 Lake View Circle', 'Mobile','AB', '6', '32312321')")
cursor.execute("INSERT INTO test VALUES (2, 'Claiborne',"
               " 'MacCrossan', '4994 Bonner Street', 'Albuquerque', 'NM', '28', '32423414')")
cursor.execute("INSERT INTO test VALUES (3, 'Amara', 'McSporon', '6595 Arapahoe Terrace', "
               "'Des Moine', 'IW', '6', '2341931')")
cursor.execute("INSERT INTO test VALUES (4, 'Antone', "
               "'Titcombe', '34 Ryan Parkway', 'Washington', 'DOC', '36385', '12312312')")

# print these

cursor.execute("SELECT * FROM test")

results = cursor.fetchall()
print(results)

cursor.execute("DELETE FROM test WHERE id=4")
cursor.execute("SELECT * FROM test")
print(cursor.fetchall())