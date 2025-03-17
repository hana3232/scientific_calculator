import tkinter as tk
from tkinter import messagebox
import math

def on_click(button_text):
    if button_text == "C":
        entry_var.set("")
    elif button_text == "=":
        try:
            expression = entry_var.get()
            entry_var.set(eval(expression))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
    else:
        entry_var.set(entry_var.get() + str(button_text))

# Create main window
root = tk.Tk()
root.title("Scientific Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), justify='right')
entry.grid(row=0, column=0, columnspan=6)

buttons = [
    ("7", "8", "9", "/", "sin", "cos"),
    ("4", "5", "6", "*", "tan", "log"),
    ("1", "2", "3", "-", "exp", "sqrt"),
    ("0", ".", "C", "+", "(", ")"),
    ("=",)
]

for r, row in enumerate(buttons):
    for c, button_text in enumerate(row):
        btn = tk.Button(root, text=button_text, font=("Arial", 14), padx=20, pady=10,
                        command=lambda text=button_text: on_click(text))
        btn.grid(row=r+1, column=c, sticky="nsew")

root.mainloop()
