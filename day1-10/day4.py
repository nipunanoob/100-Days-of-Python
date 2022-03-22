import random

game = True
options = [0,1,2]

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
tie = "You tie! Do you want to continue(y/n): "
lose = "You lose! Do you want to continue(y/n): "
win = "You win! Do you want to continue(y/n): "
hands = [rock, paper, scissors]

def display_hands(player, computer):
    print("You chose: ")
    print(hands[player])
    print("Computer chose: ")
    print(hands[computer])



while(game):
    player = int(input("Enter you choice...Type 0 for Rock, Type 1 for Paper and Type 2 for Scissors"))
    if player not in [0, 1, 2]:
        print("Invalid option")
        continue
    computer = random.randint(0,2)
    display_hands(player, computer)
    if player == 0:
        if computer == 0:
            game = input(tie).lower() == 'y'
        elif computer == 1:
            game = input(lose).lower() == 'y'
        else:
            game = input(win).lower() == 'y'
    elif player == 1:
        if computer == 1:
            game = input(tie).lower() == 'y'
        elif computer == 0:
            game = input(win).lower() == 'y'
        else:
            game = input(lose).lower() == 'y'
    else:
        if computer == 2:
            game = input(tie).lower() == 'y'
        elif computer == 0:
            game = input(lose).lower() == 'y'
        else:
            game = input(winy).lower() == 'y'