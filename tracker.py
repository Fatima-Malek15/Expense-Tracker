import sqlite3

def init_db():
    conn = sqlite3.connect("expense.db") #creates file if doesnt exist
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS expenses
    (id INTEGER PRIMARY KEY AUTO-INCREMENT,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    expense_date TEXT NOT NULL
    )""")

    conn.commit()
    conn.close()
