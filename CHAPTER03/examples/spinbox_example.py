import tkinter as tk

parent = tk.Tk()
my_double_var = tk.DoubleVar()

my_spinbox = tk.Spinbox(
    parent,
    from_=0.5,
    to=52.0,
    increment=0.01,
    textvariable=my_double_var,
)

my_spinbox.pack()
parent.mainloop()
