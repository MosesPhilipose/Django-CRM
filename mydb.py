import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Moses@2002'
)

#prepare cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE moses")

print("all done!")
