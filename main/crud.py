import sqlite3


def add_product(db, name: str, category: str, price: int):
    db.execute('''INSERT INTO products(name, category, price)
                VALUES(?, ?, ?)''', (name, category, price))
    db.commit()


def add_customer(db, name: str, last_nm: str, email: str):
    db.execute('''INSERT INTO customers(first_name, last_name, email) VALUES(?, ?, ?)''', (name, last_nm, email))
    db.commit()

def add_order(db, customer_id: int, product_id: int, quantity: int):
    db.execute('''INSERT INTO orders(customer_id, product_id, quantity, order_date)
               VALUES(?, ?, ?, CURRENT_TIMESTAMP)''', (customer_id, product_id, quantity))
    db.commit()


def total_money(db):
    total = db.execute('''SELECT SUM(products.price*orders.quantity) AS total_bill 
                       FROM orders
                       INNER JOIN products ON orders.product_id == products.product_id
                       ''')
    return total.fetchall()


def get_customers_order_count(db):
    result = db.execute('''SELECT customers.first_name AS customer_name, COUNT(orders.order_id)
                        FROM orders
                        INNER JOIN customers ON orders.customer_id == customers.customer_id
                        GROUP BY customers.first_name
                        ORDER BY customers.customer_id ASC''')
    return result.fetchall()


def avg_money(db):
    result = db.execute('''SELECT AVG(products.price*orders.quantity) AS avg_price
                        FROM orders
                        INNER JOIN products ON orders.product_id == products.product_id''')
    return result.fetchone()


def pop_category(db):
    result = db.execute('''SELECT SUM(orders.quantity), products.category FROM orders
                        INNER JOIN products ON products.product_id == orders.product_id
                        GROUP BY products.category
                        ''')
    return result.fetchone()


def total_products_in_category(db):
    result = db.execute('''SELECT products.category AS category_name, COUNT(products.product_id)
                        FROM products
                        GROUP BY products.category''')
    return result.fetchall()


def all_products(db):
    result = db.execute('''SELECT * FROM products''')
    return result.fetchall()


def all_customers(db):
    result = db.execute('''SELECT * FROM customers''')
    return result.fetchall()


def all_orders(db):
    result = db.execute('''SELECT * FROM orders''')
    return result.fetchall()

def update_prices_10(db, category):
    db.execute(f'''UPDATE products SET price = price*1.1 WHERE category = "{category}"''')
    db.commit()