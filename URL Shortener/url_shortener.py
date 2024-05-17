import tkinter as tk
import pyshorteners

def shorten_url():
    url = entry_url.get()
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    entry_short_url.delete(0, tk.END)
    entry_short_url.insert(0, short_url)

app = tk.Tk()
app.title("URL Shortener")

label_url = tk.Label(app, text="Enter URL:")
label_url.pack()

entry_url = tk.Entry(app, width=50)
entry_url.pack()

button_shorten = tk.Button(app, text="Shorten URL", command=shorten_url)
button_shorten.pack()

label_short_url = tk.Label(app, text="Short URL:")
label_short_url.pack()

entry_short_url = tk.Entry(app, width=50)
entry_short_url.pack()

app.mainloop()
