import sqlite3

connection = sqlite3.connect("Homeworks/Homework19/shop.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    price REAL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)
)
""")

cursor.execute("INSERT INTO categories (name) VALUES ('Електроніка')")
cursor.execute("INSERT INTO categories (name) VALUES ('Одяг')")
cursor.execute("INSERT INTO categories (name) VALUES ('Книги')")

cursor.execute("INSERT INTO products (name, description, price, category_id) VALUES ('Смартфон', 'Смартфон з великим екраном', 12999.99, 1)")
cursor.execute("INSERT INTO products (name, description, price, category_id) VALUES ('Ноутбук', 'Ноутбук для роботи та навчання', 24999.00, 1)")
cursor.execute("INSERT INTO products (name, description, price, category_id) VALUES ('Футболка', 'Бавовняна футболка', 399.50, 2)")
cursor.execute("INSERT INTO products (name, description, price, category_id) VALUES ('Джинси', 'Класичні джинси', 899.00, 2)")
cursor.execute("INSERT INTO products (name, description, price, category_id) VALUES ('Python для початківців', 'Книга з програмування', 349.00, 3)")

connection.commit()

join = "SELECT products.name, categories.name FROM products JOIN categories ON products.category_id = categories.id;"

connection.close()