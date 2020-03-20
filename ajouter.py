import cgi
import cgitb
import sqlite3

cgitb.enable()
form=cgi.FieldStorage()
print("Content-type:text/html;charset=utf-8\n")
html = """<!DOCTYPE html>
<head>
<title> Ajouter Utilisateur</title>
</head>
<body>
<h1> Ajouter Utilisateur</h1>
"""


print(html)
try:
    if form.getvalue("nom") and form.getvalue(("pre")) and form.getvalue("courriel") and form.getvalue("mot_de_passe") and form.getvalue("age") and form.getvalue("gouvernat") and form.getvalue("numerodetelephone"):
        nom = form.getvalue("nom")
        pre = form.getvalue("pre")
        mp = form.getvalue("mot_de_passe")
        mail = form.getvalue("courriel")
        age = form.getvalue("age")
        lieu = form.getvalue("gouvernat")
        numero = form.getvalue("numerodetelephone")
        connection = sqlite3.connect("Client.db")
        cursor = connection.cursor()
        newuser=(nom,pre,mail,mp,numero,age,lieu)

        try:
            cursor.execute('INSERT INTO client VALUES(?,?,?,?,?,?,?)', newuser)
            print("nouvel utilisateur ajoute")

        except:
            print(Exception)
            print("error exists!! \n")
            connection.commit()
            connection.close()
except:
            print("<p> Informations non transmises </p>")

html = """
</body>
</html>
"""

print(html)