import turtle
import pandas as pd

#  Set turtle shape to image
FONT = ('Calibri', 15, 'bold')
screen = turtle.Screen()
screen.title("US States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Convert csv to dataframe using pandas
df = pd.read_csv('50_states.csv')
number_of_states = len(df.index)
states = df.state

guessed_states = []

states_guessed = 0

pointer = turtle.Turtle()
pointer.hideturtle()
pointer.penup()
while len(guessed_states) < number_of_states:
    answer_state = screen.textinput(title=f"{states_guessed}/{number_of_states} States correct",
                                    prompt="Whats another state's name?").title()
    if answer_state in states.values and answer_state not in guessed_states:
        x_coor = int(df[states == answer_state].x.values)
        y_coor = int(df[states == answer_state].y.values)
        pointer.goto(x_coor, y_coor)
        pointer.write(answer_state)
        guessed_states.append(answer_state)
        states_guessed += 1

    if answer_state == 'Exit':
        states_missed = [state for state in states if state not in guessed_states]
        df2 = pd.DataFrame(states_missed)
        df2.columns = ['States']
        df2.to_csv('states_to_learn.csv')
        break

#states_to_learn.csv




