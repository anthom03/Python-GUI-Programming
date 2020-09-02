import tkinter as tk
from tkinter import ttk


class EntryForm(tk.Frame):
    """The form for entering data"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, *kwargs)

        record_details_frame = ttk.LabelFrame(self, text='Record Details')
        environment_frame = ttk.LabelFrame(self, text='Environment')
        plant_count_frame = ttk.LabelFrame(self, text='Plant Counts')
        plant_height_frame = ttk.LabelFrame(self, text='Plant Height')
        notes_frame = ttk.LabelFrame(self, text='Notes')

        blossoms_label = ttk.Label(plant_count_frame, text='Blossoms')
        date_label = ttk.Label(record_details_frame, text='Date')
        fruit_label = ttk.Label(plant_count_frame, text='Fruit')
        humidity_label = ttk.Label(environment_frame, text='Humidity')
        lab_label = ttk.Label(record_details_frame, text='Lab')
        light_label = ttk.Label(environment_frame, text='Light')
        max_height_label = ttk.Label(plant_height_frame, text='Max')
        median_height_label = ttk.Label(plant_height_frame, text='Median')
        min_height_label = ttk.Label(plant_height_frame, text='Min')
        notes_label = ttk.Label(notes_frame, text='Notes')
        plants_label = ttk.Label(plant_count_frame, text='Plants')
        plot_label = ttk.Label(record_details_frame, text='Plot')
        seed_label = ttk.Label(record_details_frame, text='Seed Sample ID')
        tech_label = ttk.Label(record_details_frame, text='Technician')
        temperature_label = ttk.Label(environment_frame, text='Temperature')
        time_label = ttk.Label(record_details_frame, text='Time')

        self.blossoms = tk.StringVar()
        blossoms_spinbox = ttk.Spinbox(plant_count_frame, textvariable=self.blossoms)
        self.date = tk.StringVar()
        date_entry = ttk.Entry(record_details_frame, textvariable=self.date)
        self.fault = tk.BooleanVar()
        fault_check = ttk.Checkbutton(environment_frame, variable=self.fault, text='Equipment Fault') # https://stackoverflow.com/questions/4236910/getting-checkbutton-state
        self.fruit = tk.StringVar()
        fruit_spinbox = ttk.Spinbox(plant_count_frame, textvariable=self.fruit)
        self.humidity = tk.StringVar()
        humidity_spinbox = ttk.Spinbox(environment_frame, textvariable=self.humidity)
        self.lab = tk.StringVar()
        lab_combobox = ttk.Combobox(record_details_frame, textvariable=self.lab)
        self.light = tk.StringVar()
        light_spinbox = ttk.Spinbox(environment_frame, textvariable=self.light)
        self.max_height = tk.StringVar()
        max_height_spinbox = ttk.Spinbox(plant_height_frame, textvariable=self.max_height)
        self.median_height = tk.StringVar()
        median_height_spinbox = ttk.Spinbox(plant_height_frame, textvariable=self.median_height)
        self.min_height = tk.StringVar()
        min_height_spinbox = ttk.Spinbox(plant_height_frame, textvariable=self.min_height)
        self.notes = tk.StringVar()
        notes_entry = tk.Entry(notes_frame, textvariable=self.notes)
        self.plants = tk.StringVar()
        plants_spinbox = ttk.Spinbox(plant_count_frame, textvariable=self.plants)
        self.plot = tk.StringVar()
        plot_combobox = ttk.Combobox(record_details_frame, textvariable=self.plot)
        self.seed = tk.StringVar()
        seed_entry = ttk.Entry(record_details_frame, textvariable=self.seed)
        self.tech = tk.StringVar()
        tech_entry = ttk.Entry(record_details_frame, textvariable=self.tech)
        self.temperature = tk.StringVar()
        temperature_spinbox = ttk.Spinbox(environment_frame, textvariable=self.temperature)
        self.time = tk.StringVar()
        time_combobox = ttk.Combobox(record_details_frame, textvariable=self.time)

        date_label.grid(row=0, column=0)
        date_entry.grid(row=1, column=0)
        time_label.grid(row=0, column=1)
        time_combobox.grid(row=1, column=1)
        lab_label.grid(row=0, column=2)
        lab_combobox.grid(row=1, column=2)
        tech_label.grid(row=2, column=0)
        tech_entry.grid(row=3, column=0)
        plot_label.grid(row=2, column=1)
        plot_combobox.grid(row=3, column=1)
        seed_label.grid(row=2, column=2)
        seed_entry.grid(row=3, column=2)
        record_details_frame.grid(row=0, column=0)

        humidity_label.grid(row=0, column=0)
        humidity_spinbox.grid(row=1, column=0)
        light_label.grid(row=0, column=1)
        light_spinbox.grid(row=1, column=1)
        temperature_label.grid(row=0, column=2)
        temperature_spinbox.grid(row=1, column=2)
        fault_check.grid(row=2, column=0)
        environment_frame.grid(row=1, column=0)

        plants_label.grid(row=0, column=0)
        plants_spinbox.grid(row=1, column=0)
        blossoms_label.grid(row=0, column=1)
        blossoms_spinbox.grid(row=1, column=1)
        fruit_label.grid(row=0, column=2)
        fruit_spinbox.grid(row=1, column=2)
        plant_count_frame.grid(row=2, column=0)

        min_height_label.grid(row=0, column=0)
        min_height_spinbox.grid(row=1, column=0)
        max_height_label.grid(row=0, column=1)
        max_height_spinbox.grid(row=1, column=1)
        median_height_label.grid(row=0, column=2)
        median_height_spinbox.grid(row=1, column=2)
        plant_height_frame.grid(row=3, column=0)

        notes_entry.grid(row=0, column=0, sticky=(tk.W + tk.E))
        notes_frame.grid(row=4, column=0, sticky=(tk.W + tk.E))

        save_button = ttk.Button(self, text='Save')
        save_button.grid(row=5, column=0, sticky=tk.E)

        self.output = tk.StringVar()
        output_label = ttk.Label(self, textvariable=self.output, wraplength=415)
        output_label.grid(row=6, column=0, sticky=(tk.N + tk.W))

        # TODO: Remove the following when save button implemented
        self.output.set('output_label')

    def on_save(self):
        # TODO: Place all info into output label
        print("Save (WIP)")


class AbqEntryApp(tk.Tk):
    """Main Application"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("ABQ Entry Application")
        self.geometry("425x400")
        self.resizable(width=False, height=False)

        EntryForm(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        # self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = AbqEntryApp()
    app.mainloop()
