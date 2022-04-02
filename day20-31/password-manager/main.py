from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().capitalize()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or password == "" or email == "":
        messagebox.showwarning(title="Seriously...", message="Please do not leave your fields empty")
    else:
        confirm = messagebox.askokcancel(title=website, message=f"These are the details entered \nEmail: {email}\n "
                                                                f"Password: {password}\n Is it ok to save?")
        if confirm:
            with open('data.txt', 'a') as file:
                file.write(f"{website} | {email} | {password}")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(475, 300)
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1, sticky='W')

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=42)
website_entry.grid(row=1, column=1, columnspan=2, sticky='W')
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=42)
email_entry.grid(row=2, column=1, columnspan=2, sticky='W')
email_entry.insert(0, 'nipunanoob@gmail.com')

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=23)
password_entry.grid(row=3, column=1, columnspan=2, sticky='W')

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=1, sticky='E', columnspan=2)

add_password_button = Button(text="Add", width=35, command=save)
add_password_button.grid(row=4, column=1, columnspan=1)

window.mainloop()
