import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password='admin')

cursor=con.cursor()

cursor.execute("create database screeing_nit")
print(cursor)