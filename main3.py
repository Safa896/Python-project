import sqlite3
connection = sqlite3.connect("Base1.db")
cursor = connection.cursor()
my_useraddress = ("Gabes",)
cursor.execute('SELECT * from USERS where useraddress=?', my_useraddress)
result2 = cursor.fetchone()[1]
print(" L'adresse d'utilisateur est :", result2)
#enregistrement d'un element dans une BD
connection.close()