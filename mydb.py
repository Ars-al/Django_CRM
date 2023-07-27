# install mysql on computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

# Database connection

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mysql123'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Craete a Database
cursorObject.execute("CREATE DATABASE crm_system")

print("All Done!")
