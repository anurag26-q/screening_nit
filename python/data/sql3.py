con= mysql.connector.connect(host="localhost",user="root",password="admin")

# cursor = con.cursor()
# cursor.execute("show databases")
# for x in cursor:
#     print(x)

if con.is_connected():
    print("Connected to MySQL database")

cursor=con.cursor()

cursor.execute("create table studnet (id int,name varchar(20))")
cursor.execute("show tables")

print(cursor)