import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(
            self.frame, width=50, height=15, selectmode=tk.SINGLE
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(
            self.button_frame, text="Add Task", width=10, command=self.add_task
        )
        self.add_button.grid(row=0, column=0, padx=5)

        self.update_button = tk.Button(
            self.button_frame, text="Update Task", width=10, command=self.update_task
        )
        self.update_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(
            self.button_frame, text="Delete Task", width=10, command=self.delete_task
        )
        self.delete_button.grid(row=0, column=2, padx=5)

        self.done_button = tk.Button(
            self.button_frame, text="Mark as Done", width=10, command=self.mark_done
        )
        self.done_button.grid(row=0, column=3, padx=5)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append({'task': task, 'done': False})
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task['done'] else "Not Done"
            self.listbox.insert(tk.END, f"{task['task']} [{status}]")

    def update_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            new_task = simpledialog.askstring(
                "Update Task", "Enter the new task:", initialvalue=self.tasks[index]['task']
            )
            if new_task:
                self.tasks[index]['task'] = new_task
                self.update_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def mark_done(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]['done'] = True
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as done.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
