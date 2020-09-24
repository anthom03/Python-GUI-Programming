import tkinter as tk
from tkinter import ttk
from CHAPTER03.homework.label_input import LabelInput


class PizzaOrderForm(tk.Frame):
    """The input form for out widgets"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # A dict to keep track of input widgets
        self.inputs = {}

        basicinfo = tk.LabelFrame(self, text='Basic Pizza Info')

        self.inputs['Quantity'] = LabelInput(basicinfo, 'Quantity', input_class=ttk.Spinbox, input_var=tk.IntVar(),
                                             input_args={'from_': 1, 'to': 99})
        self.inputs['Quantity'].grid(row=0, column=0)

        self.inputs['Size'] = LabelInput(basicinfo, 'Size', input_class=ttk.Combobox, input_var=tk.StringVar(),
                                         input_args={'values': ['Small', 'Medium', 'Large', 'Extra Large']})
        self.inputs['Size'].grid(row=0, column=1)

        self.inputs['Crust Style'] = LabelInput(basicinfo, 'Crust Style', input_class=ttk.Combobox,
                                                input_var=tk.StringVar(),
                                                input_args={'values': ['Original', 'Thin', 'Thick']})
        self.inputs['Crust Style'].grid(row=1, column=0)

        self.inputs['Pizza Sauce'] = LabelInput(basicinfo, 'Pizza Sauce', input_class=ttk.Checkbutton,
                                                input_var=tk.BooleanVar())
        self.inputs['Pizza Sauce'].grid(row=1, column=1)

        self.inputs['Cheese'] = LabelInput(basicinfo, 'Cheese', input_class=ttk.Checkbutton, input_var=tk.BooleanVar())
        self.inputs['Cheese'].grid(row=1, column=2)

        basicinfo.grid(row=0, column=0, sticky=tk.W + tk.E)

        meattoppings = tk.LabelFrame(self, text='Meat Toppings')

        self.inputs['Pepperoni'] = LabelInput(meattoppings, 'Pepperoni', input_class=ttk.Checkbutton,
                                              input_var=tk.BooleanVar())
        self.inputs['Pepperoni'].grid(row=0, column=0)

        self.inputs['Italian Sausage'] = LabelInput(meattoppings, 'Italian Sausage', input_class=ttk.Checkbutton,
                                                    input_var=tk.BooleanVar())
        self.inputs['Italian Sausage'].grid(row=0, column=1)

        self.inputs['Bacon'] = LabelInput(meattoppings, 'Bacon', input_class=ttk.Checkbutton, input_var=tk.BooleanVar())
        self.inputs['Bacon'].grid(row=0, column=2)

        self.inputs['Ham'] = LabelInput(meattoppings, 'Ham', input_class=ttk.Checkbutton, input_var=tk.BooleanVar())
        self.inputs['Ham'].grid(row=1, column=0)

        self.inputs['Meatballs'] = LabelInput(meattoppings, 'Meatballs', input_class=ttk.Checkbutton,
                                              input_var=tk.BooleanVar())
        self.inputs['Meatballs'].grid(row=1, column=1)

        self.inputs['Grilled Chicken'] = LabelInput(meattoppings, 'Grilled Chicken', input_class=ttk.Checkbutton,
                                                    input_var=tk.BooleanVar())
        self.inputs['Grilled Chicken'].grid(row=1, column=2)

        meattoppings.grid(row=1, column=0, sticky=tk.W + tk.E)

        veggietoppings = tk.LabelFrame(self, text='Veggie Toppings')

        self.inputs['Onions'] = LabelInput(veggietoppings, 'Onions', input_class=ttk.Checkbutton,
                                           input_var=tk.BooleanVar())
        self.inputs['Onions'].grid(row=0, column=0)

        self.inputs['Green Peppers'] = LabelInput(veggietoppings, 'Green Peppers', input_class=ttk.Checkbutton,
                                                  input_var=tk.BooleanVar())
        self.inputs['Green Peppers'].grid(row=0, column=1)

        self.inputs['Tomatoes'] = LabelInput(veggietoppings, 'Tomatoes', input_class=ttk.Checkbutton,
                                             input_var=tk.BooleanVar())
        self.inputs['Tomatoes'].grid(row=0, column=2)

        self.inputs['Pineapple'] = LabelInput(veggietoppings, 'Pineapple', input_class=ttk.Checkbutton,
                                              input_var=tk.BooleanVar())
        self.inputs['Pineapple'].grid(row=0, column=3)

        veggietoppings.grid(row=2, column=0, sticky=tk.E + tk.W)

        # Notes section
        self.inputs['Notes'] = LabelInput(
            self, 'Notes',
            input_class=tk.Text,
            input_args={'width': 50, 'height': 2}
        )
        self.inputs['Notes'].grid(sticky='w', row=3, column=0)

        self.reset()

    def get(self):
        data = {}
        for key, widget in self.inputs.items():
            data[key] = widget.get()
        return data

    def reset(self):
        for widget in self.inputs.values():
            widget.set('')
