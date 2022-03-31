import tkinter

def button_clicked():
    my_label['text'] = input.get()

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "italic"))

my_label.config(text="New Label")
# my_label.place(x=100,y=200)
# my_label.pack()
my_label.grid(column=0, row=0)

# Button
button = tkinter.Button(text='Click me', command=button_clicked)
button.grid(column=1, row=1)

# New Button
new_button = tkinter.Button(text='Click me', command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()
