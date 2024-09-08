import tkinter as tk
from tkinter import messagebox

def add_expense():
    try:
        
        description = description_entry.get()
        amount_str = amount_entry.get()  
        
        
        amount = float(amount_str)  
        
        
        if amount < 0:
            raise ValueError("Amount should be positive.")
        
        
        messagebox.showinfo("Success", f"Added expense: {description} - ${amount:.2f}")
        
        
        description_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        
    except ValueError as e:
        
        messagebox.showerror("Error", f"Invalid input: {e}")


root = tk.Tk()
root.title("Expense Tracker")

tk.Label(root, text="Description:").pack()
description_entry = tk.Entry(root)
description_entry.pack()

tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack()

root.mainloop()
