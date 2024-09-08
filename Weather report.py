import tkinter as tk
import sqlite3

# Setup database
conn = sqlite3.connect('expenses.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS expenses (amount REAL, category TEXT)''')
conn.commit()

def add_expense():
    amount = float(amount_entry.get())
    category = category_entry.get()
    c.execute('INSERT INTO expenses (amount, category) VALUES (?, ?)', (amount, category))
    conn.commit()
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Expense Tracker")

tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category:").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack()

root.mainloop()
