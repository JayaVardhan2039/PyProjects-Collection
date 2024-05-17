import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task.")

app = tk.Tk()
app.title('Todo List')

frame_tasks = tk.Frame(app)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(app, width=50)
entry_task.pack()

button_add_task = tk.Button(app, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tk.Button(app, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

app.mainloop()
