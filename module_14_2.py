import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'User{i}', f'example{i}@gmail.com', (i * 10), 1000))

cursor.execute("UPDATE Users SET balance = ? WHERE id % 2 != 0", (500,))

cursor.execute("DELETE FROM Users WHERE (id - 1) % 3 = 0")

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
users = cursor.fetchall()
for user in users:
    print(user)

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
cursor.execute("SELECT COUNT(*) FROM Users")
num_of_u = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
sum_of_bal = cursor.fetchone()[0]
print(sum_of_bal / num_of_u)

connection.commit()
connection.close()
