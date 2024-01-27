import sqlite3


def add_product(db, name: str, category: str, price: int):
    db.execute('''INSERT INTO products(name, category, price)
                VALUES(?, ?, ?)''', (name, category, price))
    db.commit()


def add_customer(db, name: str, last_nm: str, email: str):
    db.execute('''INSERT INTO customers(first_name, last_name, email)
                VALUES(?, ?, ?)''', (name, last_nm, email))
    db.commit()

def add_order(db, customer_id: int, product_id: int, quantity: int):
    db.execute('''INSERT INTO orders(customer_id, product_id, quantity, order_date)
               VALUES(?, ?, ?, CURRENT_TIMESTAMP)''', (customer_id, product_id, quantity))
    db.commit()

def get_customers_order_count(db):
    db.execute('''''')