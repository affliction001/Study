import sqlite3

connection = sqlite3.connect('mydatabase.db')
cursor = connection.cursor()

cursor.execute("""
		CREATE TABLE IF NOT EXISTS users
		(name text, lastname text, age integer, raiting real)
	""")

users = [
	('Bill', 'Gates', 56, 99.3),
	('Linus', 'Torvalds', 46, 100.0),
	('Steve', 'Jobs', 62, 99.5)
]

for user in users:
	cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?)", user)

connection.commit()

cursor.execute("SELECT * FROM users")
results = cursor.fetchall()

print(results)

cursor.close()
connection.close()
