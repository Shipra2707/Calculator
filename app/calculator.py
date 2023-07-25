import tkinter as tk
from math import sqrt

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_sqrt():
    current = entry.get()
    try:
        result = sqrt(eval(current))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


window = tk.Tk()
window.title("Calculator")


entry = tk.Entry(window, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = []
for i in range(1, 10):
    button = tk.Button(window, text=str(i), padx=20, pady=10, command=lambda num=i: button_click(num))
    buttons.append(button)
    buttons[i-1].grid(row=3 - (i-1)//3, column=(i-1) % 3)


operators = ['+', '-', '*', '/']
for i in range(len(operators)):
    button = tk.Button(window, text=operators[i], padx=20, pady=10, command=lambda op=operators[i]: button_click(op))
    buttons.append(button)
    buttons[-1].grid(row=4 + i, column=0)


button_clear = tk.Button(window, text="C", padx=20, pady=10, command=button_clear)
button_clear.grid(row=4, column=1)

button_zero = tk.Button(window, text="0", padx=20, pady=10, command=lambda: button_click(0))
button_zero.grid(row=4, column=2)

button_equal = tk.Button(window, text="=", padx=20, pady=10, command=button_equal)
button_equal.grid(row=5, column=0)

button_sqrt = tk.Button(window, text="√", padx=20, pady=10, command=button_sqrt)
button_sqrt.grid(row=5, column=1)


window.mainloop()
