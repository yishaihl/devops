#Import pymysql
import pymysql
import pymysql.cursors

# Establishing a connection to DB
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Qw1234!!', db='users')

# Getting a cursor from Database
cursor = conn.cursor()

# Getting all data from table “users”
cursor.execute("SELECT * FROM users.players;")

# Iterating table and printing all users
for row in cursor:
    print(row)

cursor.close()
conn.close()