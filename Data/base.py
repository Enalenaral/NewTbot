import sqlite3

connection = sqlite3.connect('progect.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS progect 
              (Surname TEXT, Name TEXT, Class INT)''')


cursor.execute("INSERT INTO progect VALUES ('Родичева','Юлия', 9)")
records = cursor.execute("SELECT * FROM progect").fetchall()
print(records)
connection.commit()
connection.close()
