import sqlite3

DATABASE_FILE = 'subscriptions.db'

def create_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscriptions (
            user_id INTEGER PRIMARY KEY,
            product TEXT,
            payment_method TEXT,
            payment_id TEXT,
            subscription_start INTEGER,
            subscription_end INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def add_subscription(user_id, product, payment_method, payment_id, subscription_start, subscription_end):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO subscriptions VALUES (?, ?, ?, ?, ?, ?)", (user_id, product, payment_method, payment_id, subscription_start, subscription_end))
    conn.commit()
    conn.close()

def check_subscription(user_id):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subscriptions WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result