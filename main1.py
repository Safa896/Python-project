import sqlite3
connection = sqlite3.connect("Base1.db")
cursor = connection.cursor()
#print(type(connection))
#print (type(cursor))
#lecture dans une BD et fermer
req = "select * from USERS"
result = cursor.execute(req)
for row in result.fetchall():
    print("nom :", row[0])
    print("adresse:", row[1])
    print("numero:", row[2])
    print("age:",row[3])



newuser = ("Fekher","Spain",2562566,22)
cursor.execute('INSERT INTO USERS VALUES(?,?,?,?)', newuser)
connection.commit()
print("Nouvel utilisateur ajouté")
#parcourir


connection.close()


