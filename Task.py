import tkinter as tk
import pickle

def load_tasks():
    try:
        with open('tasks.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

def save_tasks():
    with open('tasks.pkl', 'wb') as f:
        pickle.dump(tasks, f)

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        save_tasks()
        task_entry.delete(0, tk.END)
        update_task_list()

def update_task_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)

root = tk.Tk()
root.title("To-Do List")

tasks = load_tasks()

tk.Label(root, text="New Task:").pack()
task_entry = tk.Entry(root)
task_entry.pack()

tk.Button(root, text="Add Task", command=add_task).pack()

task_list = tk.Listbox(root)
task_list.pack()
update_task_list()

root.mainloop()

