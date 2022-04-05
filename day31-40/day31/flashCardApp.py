from tkinter import *
from appData import french_words_list
from random import randint

BACKGROUND_COLOR = "#B1DDC6"
current_card = []


def select_another_word():
    global current_card
    current_card = french_words_list[randint(0, 100)]
    print(current_card)
    french_word = current_card['French']
    cardCanvas.itemconfig(cardWord, text=french_word)


def flip_card():
    global current_card
    english_word = current_card['English']
    cardCanvas.itemconfig(cardTitle, text="English")
    cardCanvas.itemconfig(cardWord, text)


screen = Tk()
screen.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
screen.after(3000, func=flip_card)

rightSign = PhotoImage(file="images/right.png")
wrongSign = PhotoImage(file="images/wrong.png")
cardFront = PhotoImage(file="images/card_front.png")
cardBack = PhotoImage(file="images/card_back.png")

cardCanvas = Canvas(screen, width=800, height=535, background=BACKGROUND_COLOR, highlightthickness=0)
cardCanvas.create_image(410, 275, image=cardFront, anchor=CENTER)
cardTitle = cardCanvas.create_text(400, 150, text="French", font=('Arial', 40, 'italic'))
cardWord = cardCanvas.create_text(400, 253, text=french_words_list[randint(0, 100)]['French'], font=('Arial', 60, 'bold'))
cardCanvas.grid(row=0, columnspan=2, column=0)

wrongButton = Button(image=wrongSign, borderwidth=0, highlightthickness=0, command=select_another_word)
wrongButton.grid(row=1, column=0)

rightButton = Button(image=rightSign, borderwidth=0, highlightthickness=0, command=select_another_word)
rightButton.grid(row=1, column=1)

screen.mainloop()
