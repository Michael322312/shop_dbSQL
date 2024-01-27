import sqlite3
import crud

db = sqlite3.connect("shop.db")

db.execute('''CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL);''')

db.execute('''CREATE TABLE  IF NOT EXISTS customers ( customer_id INTEGER PRIMARY KEY AUTOINCREMENT, 
           first_name TEXT NOT NULL, last_name TEXT NOT NULL,
           email TEXT NOT NULL UNIQUE);''')

db.execute('''CREATE TABLE  IF NOT EXISTS orders ( order_id INTEGER PRIMARY KEY AUTOINCREMENT,
           customer_id INTEGER NOT NULL, product_id INTEGER NOT NULL,
           quantity INTEGER NOT NULL, order_date DATE NOT NULL,
           FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
           FOREIGN KEY (product_id) REFERENCES products(product_id));''')


while True:

    print('''
    Що ви хочете зробити?

    1 - Додавання продуктів:
    2 - Додавання клієнтів:
    3 - Замовлення товарів:
    4 - Сумарний обсяг продажів:
    5 - Кількість замовлень на кожного клієнта:
    6 - Середній чек замовлення:
    7 - Найбільш популярна категорія товарів:
    8 - Загальна кількість товарів кожної категорії:
    9 - Оновлення цін категорії на 10% більші:
    10 - Показати усіх користувачів
    11 - Показати усі продукти
    12 - Показати усі замовлення(Joined)
    0 - Вийти:''')

    command = input("Оберіть ваші дії: ")
    match command:
        case "0":
            break
        case '1':
            name = input("Name:")
            category = input("Category:")
            price = int(input('Price:'))
            crud.add_product(db, name, category, price)
        case '2':
            name = input("First name:")
            last_nm = input("Last name:")
            email = input('Email:')
            crud.add_customer(db, name, last_nm, email)
        case '3':
            customer_id = int(input("Customer ID:"))
            product_id = int(input("Product ID:"))
            quantity = int(input('Quantity:'))

            crud.add_order(db, customer_id, product_id, quantity)
        case '4':
            print(crud.total_money(db))
        case "5":
            print(crud.get_customers_order_count(db))
        case "6":
            print(crud.avg_money(db))
        case "7":
            print(crud.pop_category(db))
        case "8":
            print(crud.total_products_in_category(db))
        case "9":
            category = input("Enter category:")
            crud.update_prices_10(db, category)
        case "10":
            print(crud.all_customers(db))
        case "11":
            print(crud.all_products(db))
        case "12":
            print(crud.all_orders(db))
