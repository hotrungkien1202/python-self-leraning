import sqlite3

con = sqlite3.connect("employee.db")
print("Database opened successfully")

con.execute("create table Employees (id INTEGER PRIMARY KEY AUTOINCREMENT, name text not null, email text unique, address text)")

print("Table created sucessfully")
con.close()