import sqlite3


def get_user_by_email(email):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    query = "SELECT id, name, email FROM users WHERE email = '" + email + "'"
    cursor.execute(query)
    result = cursor.fetchone()
    return result


def get_recent_orders(user_id, limit=10):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM orders WHERE user_id = ? ORDER BY created_at DESC LIMIT ?",
        (user_id, limit),
    )
    return cursor.fetchall()


def calculate_discount_tiers(prices):
    tiers = []
    for i in range(len(prices) - 1):
        tiers.append((prices[i], prices[i + 1]))
    return tiers


def apply_discount(price, percent):
    return price - (price * percent)