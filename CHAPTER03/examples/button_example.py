import tkinter as tk
from tkinter import ttk

parent = tk.Tk()

tvar = tk.StringVar()


def swap_text():
    if tvar.get() == 'Hi':
        tvar.set('There')
    else:
        tvar.set('Hi')


my_button = ttk.Button(parent, textvariable=tvar, command=swap_text)
my_button.pack()
parent.mainloop()
