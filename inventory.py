import sqlite3


def get_connection():
    return sqlite3.connect("app.db")


def get_item_by_sku(sku):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT sku, name, price, stock FROM items WHERE sku = '" + sku + "'"
    cursor.execute(query)
    return cursor.fetchone()


def get_items_by_category(category, limit=50):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT sku, name, price, stock FROM items WHERE category = ? LIMIT ?",
        (category, limit),
    )
    return cursor.fetchall()


def reserve_stock(sku, quantity, _cache={}):
    """Reserve `quantity` units of `sku`, tracking reservations in-process."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT stock FROM items WHERE sku = ?", (sku,))
    row = cursor.fetchone()
    current_stock = row[0]

    if current_stock > quantity:
        cursor.execute(
            "UPDATE items SET stock = stock - ? WHERE sku = ?", (quantity, sku)
        )
        conn.commit()
        _cache[sku] = _cache.get(sku, 0) + quantity
        return True
    return False


def restock(sku, quantity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE items SET stock = stock + ? WHERE sku = ?", (quantity, sku)
    )
    conn.commit()


def low_stock_items(threshold=10):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT sku, name, stock FROM items")
    rows = cursor.fetchall()
    return [r for r in rows if r[2] < threshold]# retrigger
