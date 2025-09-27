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
    cursor.execute("""INSERT INTO expenses
                    (category, amount, expense_date)
                   VALUES(?,?,?)""",
                   (category, amount, expense_date))
    conn.commit()
    conn.close()
    print("Expense added")

#view expenses
def view_expense():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

#reports(basic analysis)
def summary_by_category():
    conn = sqlite3.connect("expense.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT category, SUM(amount)
                    FROM expenses
                    GROUP BY category""")
    rows = cursor.fetchall()
    for row in rows:
        print(f"{row[0]}: {row[1]}")
    conn.close()

#CLI menu
def main():
    init_db()
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summary by Category")
        print("4. Exit")

        choice = input("Choose an option ")

        if choice == "1":
            cat = input("Category: ")
            amt = float(input("Amount: "))
            date = input("Date(YYYY-MM-DD: ")
            add_expense(cat, amt,date)
        elif choice == "2":
            view_expense()
        elif choice == "3":
            summary_by_category()
        elif choice == "4":
            exit(0)
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

