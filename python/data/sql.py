import mysql.connector

con= mysql.connector.connect(host="localhost",user="root",password="admin")

# cursor = con.cursor()
# cursor.execute("show databases")
# for x in cursor:
#     print(x)

if con.is_connected():
    print("Connected to MySQL database")

cursor=con.cursor()
cursor.execute("show databases")
for x in cursor:
    print(x)

print(con)
print(100*"=")
print(con.is_connected())
print(100*"=")
print(cursor)