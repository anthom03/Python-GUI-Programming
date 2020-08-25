import tkinter as tk
from tkinter import ttk


class MathView(tk.Frame):
    """A frame that does some math"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.x = tk.IntVar()
        self.y = tk.IntVar()
        self.sum_string = tk.StringVar()
        self.sum_string.set("Sum: 0")

        x_entry = ttk.Entry(self, textvariable=self.x)
        y_entry = ttk.Entry(self, textvariable=self.y)

        math_button = ttk.Button(self, text="Math", command=self.math)
        sum_label = ttk.Label(self, textvariable=self.sum_string, font=("TkDefaultFont", 24))

        x_entry.grid(row=0, column=0, sticky=tk.W)
        y_entry.grid(row=0, column=1, sticky=tk.W)
        math_button.grid(row=0, column=2, sticky=tk.E)
        sum_label.grid(row=1, column=0, columnspan=3)

        self.columnconfigure(1, weight=0)

    def math(self):
        self.sum_string.set(f"Sum: {self.x.get() + self.y.get()}")
