import json
import tkinter as tk
from tkinter import messagebox, ttk

TASKS_FILE = "tasks.json"

class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "completed": self.completed,
        }

def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as f:
            return [Task(**d) for d in json.load(f)]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump([t.to_dict() for t in tasks], f, indent=4)

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Personal To-Do List")
        self.root.geometry("500x600")
        self.root.configure(bg="#f7f7f7")

        self.tasks = load_tasks()

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="white", fieldbackground="white", rowheight=25)
        style.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'))

        title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="#f7f7f7", fg="#333")
        title_label.pack(pady=10)

        filter_frame = tk.Frame(root, bg="#f7f7f7")
        filter_frame.pack(pady=5)

        tk.Label(filter_frame, text="Filter:", bg="#f7f7f7").pack(side=tk.LEFT, padx=5)
        self.filter_var = tk.StringVar()
        self.filter_var.set("All")
        filter_options = ["All", "Completed", "Pending"] + list(set(t.category for t in self.tasks))
        self.filter_menu = ttk.Combobox(filter_frame, textvariable=self.filter_var, values=filter_options, state="readonly", width=20)
        self.filter_menu.pack(side=tk.LEFT)
        self.filter_menu.bind("<<ComboboxSelected>>", lambda e: self.refresh_task_list())

        frame = tk.Frame(root, bg="#f7f7f7")
        frame.pack(pady=5)

        tk.Label(frame, text="Title:", bg="#f7f7f7").grid(row=0, column=0, sticky="w")
        self.title_entry = tk.Entry(frame, width=30)
        self.title_entry.grid(row=0, column=1, pady=3)

        tk.Label(frame, text="Category:", bg="#f7f7f7").grid(row=1, column=0, sticky="w")
        self.category_entry = tk.Entry(frame, width=30)
        self.category_entry.grid(row=1, column=1, pady=3)

        tk.Label(frame, text="Description:", bg="#f7f7f7").grid(row=2, column=0, sticky="nw")
        self.desc_text = tk.Text(frame, height=3, width=22)
        self.desc_text.grid(row=2, column=1, pady=3)

        tk.Button(frame, text="➕ Add Task", command=self.add_task, bg="#4caf50", fg="white", width=20).grid(row=3, column=1, pady=5)

        self.tree = ttk.Treeview(root, columns=('Title', 'Category', 'Status'), show='headings')
        self.tree.heading('Title', text='Title')
        self.tree.heading('Category', text='Category')
        self.tree.heading('Status', text='Status')

        self.tree.column('Title', width=180)
        self.tree.column('Category', width=100)
        self.tree.column('Status', width=80)

        self.tree.pack(pady=10)

        btn_frame = tk.Frame(root, bg="#f7f7f7")
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="✅ Mark Completed", command=self.mark_completed, bg="#2196f3", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="🗑️ Delete Task", command=self.delete_task, bg="#f44336", fg="white").grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="💾 Save & Exit", command=self.save_and_exit, bg="#9c27b0", fg="white").grid(row=0, column=2, padx=5)

        self.refresh_task_list()

    def add_task(self):
        title = self.title_entry.get()
        desc = self.desc_text.get("1.0", tk.END).strip()
        cat = self.category_entry.get()
        if title and cat:
            self.tasks.append(Task(title, desc, cat))
            self.title_entry.delete(0, tk.END)
            self.desc_text.delete("1.0", tk.END)
            self.category_entry.delete(0, tk.END)
            filter_options = ["All", "Completed", "Pending"] + list(set(t.category for t in self.tasks))
            self.filter_menu['values'] = filter_options
            self.refresh_task_list()
        else:
            messagebox.showwarning("Missing Data", "Title and Category are required.")

    def refresh_task_list(self):
        self.tree.delete(*self.tree.get_children())
        selected_filter = self.filter_var.get() if hasattr(self, 'filter_var') else "All"

        for i, task in enumerate(self.tasks):
            status = "✔ Done" if task.completed else "✘ Pending"
            tag = "done" if task.completed else "pending"

            if selected_filter == "Completed" and not task.completed:
                continue
            elif selected_filter == "Pending" and task.completed:
                continue
            elif selected_filter not in ["All", "Completed", "Pending"] and task.category != selected_filter:
                continue

            self.tree.insert('', 'end', iid=i, values=(task.title, task.category, status), tags=(tag,))

        self.tree.tag_configure('done', background='#d0f0c0')
        self.tree.tag_configure('pending', background='#ffe4e1')

    def mark_completed(self):
        selected = self.tree.selection()
        if selected:
            idx = int(selected[0])
            self.tasks[idx].completed = True
            self.refresh_task_list()

    def delete_task(self):
        selected = self.tree.selection()
        if selected:
            idx = int(selected[0])
            del self.tasks[idx]
            self.refresh_task_list()

    def save_and_exit(self):
        save_tasks(self.tasks)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
