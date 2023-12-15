import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.iconbitmap("resources/favicon.ico")

      
        self.tasks = []

        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5, pady=10)

        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            self.show_warning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task = self.tasks.pop(selected_task_index[0])
            self.task_listbox.delete(selected_task_index)
        else:
            self.show_warning("Warning", "Please select a task to delete.")

    def show_warning(self, title, message):
        messagebox.showwarning(title, message)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
