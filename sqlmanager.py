import sqlite3 as sql

con = sql.connect("Pyth")
con.execute("create table data(username varchar(30) primary key ,hashVal varchar(100),num int)")
# con.execute("drop table data")
