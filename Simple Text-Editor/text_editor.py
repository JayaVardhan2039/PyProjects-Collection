import tkinter as tk
from tkinter import filedialog, Text
from tkinter import messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.root.configure(bg='#2e2e2e')

        # Set up the text widget with dark mode styling
        self.text = Text(root, undo=True, bg='#1e1e1e', fg='#ffffff', insertbackground='white', 
                         selectbackground='#444444', selectforeground='#ffffff', font=("Consolas", 12))
        self.text.pack(fill=tk.BOTH, expand=1)

        # Set up the menu with dark mode styling
        self.menu = tk.Menu(root, bg='#2e2e2e', fg='#ffffff', activebackground='#444444', activeforeground='#ffffff')
        root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0, bg='#2e2e2e', fg='#ffffff', activebackground='#444444', activeforeground='#ffffff')
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)

        self.edit_menu = tk.Menu(self.menu, tearoff=0, bg='#2e2e2e', fg='#ffffff', activebackground='#444444', activeforeground='#ffffff')
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.edit_menu.add_command(label="Undo", command=self.text.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text.edit_redo)

    def new_file(self):
        self.text.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.text.get(1.0, tk.END))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    def cut_text(self):
        self.copy_text()
        self.text.delete("sel.first", "sel.last")

    def copy_text(self):
        self.text.clipboard_clear()
        self.text.clipboard_append(self.text.get("sel.first", "sel.last"))

    def paste_text(self):
        self.text.insert(tk.INSERT, self.text.clipboard_get())

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
