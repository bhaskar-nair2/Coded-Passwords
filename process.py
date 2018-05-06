import main as mn
import sqlite3 as sql

con=sql.connect("Pyth")

usr=input("Username: ")
pas=input("Password: ")

val=mn.data(usr,pas)
x=mn.data.maker(val)

con.execute("insert into data values ('"+usr+"','"+x["hash"]+"','"+str(x["num"])+"')")
con.commit()