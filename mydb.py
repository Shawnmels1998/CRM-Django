import pymysql

dataBase = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Sean@2022'
)


#prepare cursor object
cursorObject= dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE elderco")

print("ALL DONE!!")