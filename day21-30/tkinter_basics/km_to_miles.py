from tkinter import *

def calculate():
    km = int(km_entry.get())
    miles_label['text'] = round(km / 1.609, 2)


window = Tk()
window.title("Km to Miles Converter")
window.minsize(width=300, height=100)
window.config(padx=40, pady=40)

km_entry = Entry()
km_entry.grid(column=1, row=0)

km_unit_label = Label(text="Km")
km_unit_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

miles_label = Label(text="0")
miles_label.grid(column=1, row=1)

miles_unit_label = Label(text="Miles")
miles_unit_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)


window.mainloop()