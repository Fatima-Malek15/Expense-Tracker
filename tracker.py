import sqlite3

def init_db():
    conn = sqlite3.connect("expense.db") #creates file if doesnt exist
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS expenses
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    expense_date TEXT NOT NULL
    )""")

    conn.commit()
    conn.close()
if __name__ == "__main__":
    init_db()
    print("Database initialized")

#add new expense function
def add_expense(category, amount, expense_date):
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses"
                   "(category, amount, expense_date "
                   "VALUES(?, ?, ?)",
                   (category,amount, expense_date))
    conn.commit()
    conn.close()
    print("Expense added")

