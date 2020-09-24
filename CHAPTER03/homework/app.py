import csv
from datetime import datetime
import os
import tkinter as tk
from tkinter import ttk
from CHAPTER03.homework.form import PizzaOrderForm


class Application(tk.Tk):
    """Application root window"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Pizza Order Form')
        self.resizable(width=False, height=False)

        ttk.Label(
            self,
            text="Pizza Order Form",
            font=("TkDefaultFont", 16)
        ).grid(row=0)

        self.recordform = PizzaOrderForm(self)
        self.recordform.grid(row=1, padx=10)

        self.savebutton = ttk.Button(self, text='Save', command=self.on_save)
        self.savebutton.grid(sticky=tk.E, row=2, padx=10)

        # status bar
        self.status = tk.StringVar()
        self.statsbar = ttk.Label(self, textvariable=self.status)
        self.statsbar.grid(sticky=(tk.W + tk.E), row=3, padx=10)

        self.records_saved = 0

    def on_save(self):
        datestring = datetime.today().strftime("%Y-%m-%d")
        filename = 'pizza_orders_{}.csv'.format(datestring)
        newfile = not os.path.exists(filename)

        data = self.recordform.get()

        with open(filename, 'a') as fh:
            csvwriter = csv.DictWriter(fh, fieldnames=data.keys())
            if newfile:
                csvwriter.writeheader()
            csvwriter.writerow(data)

        self.records_saved += 1
        self.status.set(f"{self.records_saved} pizza orders saved this session")
        self.recordform.reset()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
