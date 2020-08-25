import tkinter as tk
from CHAPTER01.homework.hello_view import HelloView
from CHAPTER01.homework.math_view import MathView


class MyApplication(tk.Tk):
    """Main Application"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hello Tkinter")
        self.geometry("800x600")
        self.resizable(width=False, height=False)

        HelloView(self).grid(row=0, sticky=(tk.E + tk.W + tk.N))
        MathView(self).grid(row=1, sticky=(tk.E + tk.W + tk.S))
        self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()