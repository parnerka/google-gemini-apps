# Code to create a database

import sqlite3

# Connect to the database
connection = sqlite3.connect('student.db')

# Create a cursor to execute SQL commands
cursor = connection.cursor()

# Create a table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""
cursor.execute(table_info)

# Insert data into the table
cursor.execute("INSERT INTO STUDENT VALUES('Rahul', 'CS101', 'A', 90)")
cursor.execute("INSERT INTO STUDENT VALUES('Ravi', 'CS101', 'B', 85)")
cursor.execute("INSERT INTO STUDENT VALUES('Vijay', 'CS402', 'A', 35)")
cursor.execute("INSERT INTO STUDENT VALUES('Raj', 'CS402', 'B', 50)")
cursor.execute("INSERT INTO STUDENT VALUES('Varun', 'DS552', 'A', 93)")
cursor.execute("INSERT INTO STUDENT VALUES('Ram', 'DS552', 'B', 88)")
cursor.execute("INSERT INTO STUDENT VALUES('Manoj', 'CS101', 'B', 75)")

# Display the data
print("Data in the table:")
data = cursor.execute("SELECT * FROM STUDENT")

for row in data:
    print(row)

# Close the connection
connection.commit()
connection.close()

