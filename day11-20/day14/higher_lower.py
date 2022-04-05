import art
import game_data
import random
import os

logo = art.logo
vs_art = art.vs
data = game_data.data 
game = True
score = 0
insta1 = data[random.randint(0,49)]
guessed_once = False

while(game):
    os.system('cls')
    insta2 = data[0]
    insta2 = data[random.randint(0,49)]
    if insta1['follower_count'] > insta2['follower_count']:
        correct_choice = 'A'
    elif insta1['follower_count'] > insta2['follower_count']:
        correct_choice = 'B'
    else:
        correct_choice = 'AB'
    print(logo)
    if guessed_once:
        print(f"You're right! Current score: {score}")
    print(f"Choice A: {insta1['name']}, a {insta1['description']}, from {insta1['country']}")
    print(vs_art)
    print(f"Choice B: {insta2['name']}, a {insta2['description']}, from {insta2['country']}")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if guessed_once == False:
        guessed_once = True
    if choice in correct_choice:
        score += 1
        insta1 = insta2
        print(score)
    else:
        os.system('cls')
        print(logo)
        print(f"Sorry, that's wrong;. Final Score: {score}")
        game = False
