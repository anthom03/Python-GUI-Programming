import tkinter as tk

parent = tk.Tk()
my_text = tk.Text(parent)
my_text.insert('1.0', 'Look at that!!!')
my_text.insert('1.12', ', REALLY')
text = my_text.get('1.0', tk.END)
print(text)

my_text.delete('end - 3 chars')

my_text.pack()
parent.mainloop()
