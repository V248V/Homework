import sqlite3


connection = sqlite3.connect('database.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    connection.commit()



def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products

def insert_prod():
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                       (f'Pencil {i}', f'Pencil № {i}', i * 100))
    connection.commit()


if __name__ == '__main__':
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    initiate_db()
    insert_prod()

    connection.close()