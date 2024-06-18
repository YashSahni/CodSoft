class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        return f"[{'x' if self.completed else ' '}] {self.description}"

tasks = []

def add_task(description):
    task = Task(description)
    tasks.append(task)

def update_task(index, new_description):
    if 0 <= index < len(tasks):
        tasks[index].description = new_description

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def mark_task_complete(index):
    if 0 <= index < len(tasks):
        tasks[index].mark_complete()

def list_tasks():
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def main():
    while True:
        print("\nTo-Do List:")
        list_tasks()
        print("\nOptions:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter the task description: ")
            add_task(description)
        elif choice == "2":
            index = int(input("Enter the task number to update: ")) - 1
            new_description = input("Enter the new description: ")
            update_task(index, new_description)
        elif choice == "3":
            index = int(input("Enter the task number to delete: ")) - 1
            delete_task(index)
        elif choice == "4":
            index = int(input("Enter the task number to mark complete: ")) - 1
            mark_task_complete(index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.task_listbox = tk.Listbox(self.frame, height=10, width=50)
        self.task_listbox.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(Task(task))
            self.update_task_listbox()
            self.entry.delete(0, tk.END)

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index].mark_complete()
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to complete.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, str(task))

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()


import sqlite3

def init_db():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY, description TEXT, completed INTEGER)''')
    conn.commit()
    conn.close()

def add_task_to_db(description):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (description, completed) VALUES (?, 0)", (description,))
    conn.commit()
    conn.close()

def get_tasks_from_db():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, description, completed FROM tasks")
    tasks = c.fetchall()
    conn.close()
    return tasks

def update_task_in_db(task_id, new_description):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("UPDATE tasks SET description = ? WHERE id = ?", (new_description, task_id))
    conn.commit()
    conn.close()

def delete_task_from_db(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def mark_task_complete_in_db(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
