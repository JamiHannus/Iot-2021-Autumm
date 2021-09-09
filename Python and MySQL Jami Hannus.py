# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:30:45 2021

@author: Jami

Learn how to

Create database
Create table
Insert record
Select data
 using Python. As a result, show the Python source code.
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="test",
  password="test"
)
print(mydb)
db = mydb.cursor()
db.execute("CREATE DATABASE mydatabase")
## Creates a database
db.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255))")
## create table with users

sql = "INSERT INTO customers (name, email) VALUES (%s, %s)"
val = ("Jami", "jami@email.com")
db.execute(sql, val)
## commit seems to be importnat to add...
mydb.commit()
print(db.rowcount, "how many rows inserted.")
## select stuff

db.execute("SELECT * FROM users")
result = db.fetchall()
for x in result:
    print(x)
    