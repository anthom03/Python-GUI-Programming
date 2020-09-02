import tkinter as tk
from tkinter import ttk

parent = tk.Tk()
my_string_var = tk.StringVar()

combobox = ttk.Combobox(
    parent,
    textvariable=my_string_var,
    values=['Black', 'White', 'Green', 'Blue', 'Gray', 'Red', 'Yellow', 'Cyan', 'Magenta']
)

combobox.pack()
parent.mainloop()
