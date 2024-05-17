import tkinter as tk

def on_button_click(char):
    if char == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, 'Error')
    elif char == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, char)

app = tk.Tk()
app.title('Calculator')

entry = tk.Entry(app, width=16, font=('Arial', 24), bd=8, insertwidth=4, bg="powder blue", justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row = 1
col = 0
for button in buttons:
    tk.Button(app, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda char=button: on_button_click(char)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

app.mainloop()
