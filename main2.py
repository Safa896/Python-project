import sqlite3
connection=sqlite3.connect("Base1.db")
cursor = connection.cursor()
#print(type(connection))
#print (type(cursor))
#lecture dans une BD et fermer
my_username=("safa",)
cursor.execute('SELECT * from USERS where username= "safa" ')
result = cursor.fetchone()[0]
print(" Le nom d'utilisateur est :", result)
connection.close()