
"""Une autre version  avec la prise ne charge des exceptions et le rollback  de la Base de données
en cas erreur ; afin de garder la cohérence de cette dernière"""
import sqlite3
try:
    connection = sqlite3.connect("Base1.db")
    cursor = connection.cursor()
    req = cursor.execute('SELECT * from users')
    for row in req.fetchall():
        # print (row)
        print(row[1])
except Exception as e:
    print ("[ERREUR]",e)
    connection.rollback()
finally:
    connection.close()