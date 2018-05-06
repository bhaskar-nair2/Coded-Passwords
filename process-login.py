import sqlite3 as sql
import main as mn

con=sql.connect("Pyth")

usr=input("Username: ")
pas=input("Password: ")

cur=con.execute("select * from data where username='"+usr+"'")
var=cur.fetchall()
print(mn.data.retrive(var[0][0],pas,var[0][1],var[0][2]))