from numpy import diff
import art
import random

logo = art.logo


print(logo)
print("Welcome to number guessing game")
chosen_number = random.randint(1,100)
print("I'm thinking of a number between 1 and 100.")
while(True):
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        lives = 10
        break
    elif difficulty == 'hard':
        lives = 5
        break
    else:
        print("Invalid option, Try again !!!")
while lives > 0:
    print(f"You have {lives} attempts left to guess the number.")
    guess = int(input("Enter your guess: "))
    lives-=1
    if guess == chosen_number:
        print(f"You guessed the number, it was {chosen_number}\n")
        break
    elif guess < chosen_number:
        print("Guess higher")
    else:
        print("Guess lower")

if lives == 0:
    print(f"You have ran out of lives, the correct answer was {chosen_number}\n")