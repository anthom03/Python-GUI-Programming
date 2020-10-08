import tkinter as tk
from datetime import datetime
from tkinter import ttk

from chapter04a.date_entry import DateEntry
from chapter04a.label_input import LabelInput
from chapter04a.required_entry import RequiredEntry
from chapter04a.validated_combobox import ValidatedCombobox
from chapter04a.validated_spinbox import ValidatedSpinbox


class DataRecordForm(tk.Frame):
    """The input form for out widgets"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # A dict to keep track of input widgets
        self.inputs = {}

        recordinfo = tk.LabelFrame(self, text="Record Information")

        self.inputs['Date'] = LabelInput(recordinfo, 'Date', input_class=DateEntry, input_var=tk.StringVar())
        self.inputs['Date'].grid(row=0, column=0)

        self.inputs['Time'] = LabelInput(recordinfo, 'Time', input_class=ValidatedCombobox, input_var=tk.StringVar(), input_args={"values": ['8:00', '12:00', '16:00', '20:00']})
        self.inputs['Time'].grid(row=0, column=1)

        self.inputs['Technician'] = LabelInput(recordinfo, 'Technician', input_class=RequiredEntry, input_var=tk.StringVar())
        self.inputs['Technician'].grid(row=0, column=2)

        # line 2
        self.inputs['Lab'] = LabelInput(recordinfo, 'Lab', input_class=ValidatedCombobox, input_var=tk.StringVar(), input_args={'values': ['A', 'B', 'C', 'D', 'E']})
        self.inputs['Lab'].grid(row=1, column=0)

        self.inputs['Plot'] = LabelInput(recordinfo, 'Plot', input_class=ValidatedCombobox, input_var=tk.StringVar(), input_args={'values': [str(x) for x in range(1, 21)]})
        self.inputs['Plot'].grid(row=1, column=1)

        self.inputs['Seed sample'] = LabelInput(recordinfo, 'Seed sample', input_class=RequiredEntry, input_var=tk.StringVar())
        self.inputs['Seed sample'].grid(row=1, column=2)

        recordinfo.grid(row=0, column=0, sticky=tk.W + tk.E)

        # Environment Data
        environmentinfo = tk.LabelFrame(self, text='Environment Data')
        self.inputs['Humidity'] = LabelInput(environmentinfo, 'Humidity (g/m^3)', input_class=ValidatedSpinbox, input_var=tk.DoubleVar(), input_args={'from_': '0.5', 'to': '52.0', 'increment': '.01'})
        self.inputs['Humidity'].grid(row=0, column=0)

        self.inputs['Light'] = LabelInput(
            environmentinfo, "Light (klx)",
            input_class=ValidatedSpinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": '0', "to": '100', "increment": '.01'}
        )
        self.inputs['Light'].grid(row=0, column=1)

        self.inputs['Temperature'] = LabelInput(
            environmentinfo, "Temperature (°C)",
            input_class=ValidatedSpinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": '4', "to": '40', "increment": '.01'}
        )
        self.inputs['Temperature'].grid(row=0, column=2)

        self.inputs['Equipment Fault'] = LabelInput(
            environmentinfo, "Equipment Fault",
            input_class=ttk.Checkbutton,
            input_var=tk.BooleanVar()
        )
        self.inputs['Equipment Fault'].grid(row=1, column=0, columnspan=3)

        environmentinfo.grid(row=1, column=0, sticky="we")

        plantinfo = tk.LabelFrame(self, text='Plant Data')

        self.inputs['Plants'] = LabelInput(
            plantinfo, 'Plants',
            input_class=ValidatedSpinbox,
            input_var=tk.IntVar(),
            input_args={'from_': '0', 'to': '20'})
        self.inputs['Plants'].grid(row=0, column=0)

        self.inputs['Blossoms'] = LabelInput(
            plantinfo, 'Blossoms',
            input_class=ValidatedSpinbox,
            input_var=tk.IntVar(),
            input_args={'from_': '0', 'to': '1000'})
        self.inputs['Blossoms'].grid(row=0, column=1)

        self.inputs['Fruit'] = LabelInput(
            plantinfo, "Fruit",
            input_class=ValidatedSpinbox,
            input_var=tk.IntVar(),
            input_args={"from_": '0', "to": '1000'}
        )
        self.inputs['Fruit'].grid(row=0, column=2)

        # Height data
        # create variables to be updates for min/max height
        # they can be referenced for min/max variables
        min_height_var = tk.DoubleVar(value='-infinity')
        max_height_var = tk.DoubleVar(value='infinity')

        self.inputs['Min Height'] = LabelInput(
            plantinfo, 'Min Height (cm)',
            input_class=ValidatedSpinbox,
            input_var=tk.DoubleVar(),
            input_args={
                'from_': '0', 'to': '1000', 'increment': '.01',
                'max_var': max_height_var, 'focus_update_var': min_height_var
            }
        )
        self.inputs['Min Height'].grid(row=1, column=0)

        self.inputs['Max Height'] = LabelInput(
            plantinfo, "Max Height (cm)",
            input_class=ValidatedSpinbox,
            input_var=tk.DoubleVar(),
            input_args={"from_": '0', "to": '1000', "increment": '.01',
                        "min_var": min_height_var,
                        "focus_update_var": max_height_var}
        )
        self.inputs['Max Height'].grid(row=1, column=1)

        self.inputs['Median Height'] = LabelInput(
            plantinfo, 'Median Height (cm)',
            input_class=ValidatedSpinbox,
            input_var=tk.DoubleVar(),
            input_args={
                'from_': '0', 'to': '1000', 'increment': '.01',
                'min_var': min_height_var, 'max_var': max_height_var
            }
        )
        self.inputs['Median Height'].grid(row=1, column=2)

        plantinfo.grid(row=2, column=0, sticky="we")

        # Notes section
        self.inputs['Notes'] = LabelInput(
            self, 'Notes',
            input_class=tk.Text,
            input_args={'width': 75, 'height': 10}
        )
        self.inputs['Notes'].grid(sticky='w', row=3, column=0)

        self.reset()

    def get(self):
        data = {}
        for key, widget in self.inputs.items():
            data[key] = widget.get()
        return data

    def reset(self):
        """Resets the form entries"""
        # gather the values to keep for each lab
        lab = self.inputs['Lab'].get()
        time = self.inputs['Time'].get()
        technician = self.inputs['Technician'].get()
        plot = self.inputs['Plot'].get()
        plot_values = self.inputs['Plot'].input.cget('values')

        # clear all values
        for widget in self.inputs.values():
            widget.set('')

        current_date = datetime.today().strftime('%Y-%m-%d')
        self.inputs['Date'].set(current_date)
        self.inputs['Time'].input.focus()

        # check if we need to put our values beck, then do it
        if plot not in ('', plot_values[-1]):
            self.inputs['Lab'].set(lab)
            self.inputs['Time'].set(time)
            self.inputs['Technician'].set(technician)
            next_plot_index = plot_values.index(plot) + 1
            self.inputs['Plot'].set(plot_values[next_plot_index])
            self.inputs['Seed sample'].input.focus()

    def get_errors(self):
        """Get a list of field errors in the form"""

        errors = {}
        for key, widget in self.inputs.items():
            if hasattr(widget.input, 'trigger_focusout_validation'):
                widget.input.trigger_focusout_validation()
            if widget.error.get():
                errors[key] = widget.error.get()

        return errors
