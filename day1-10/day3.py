print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
game_over = "Game Over!"
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You come across a sign which tells you that treasure can be found by going thorugh one of these paths. Type left or right to continue:")
option = input().lower()
if option == 'left':
    print("You come across a strange looking river that you could swim across if you want to get the treasure.\n Do you take the plunge? Type swim or wait to continue")
    option = input().lower()
    if option == 'wait':
        print("You decided to wait and see what happens.\n A ghost approaches you to warn you that the river can only be crossed if you possess a ring to thwart the effects of the cursed river.")
        print("The ghost gives you the ring which allows yous to cross the river\nYou come across three doors, type to select red, blue or yellow door")
        option = input().lower()
        if option == 'red':
            print("A cannon ball comes flying and hits you in the head, decaptitating you in the process")
            print(game_over)
        elif option == 'yellow':
            print("You find the treasure\n YOU WIN!")
        else:
            print("You get impaled by a group of goblins")
            print(game_over)
    else:
        print("You decide to swim across the river. The river turns skin into mush, maybe you should have waited lol")
        print(game_over)
else:
    print("You come across a statue that seems to be watching you and suddenly lunges at you and detaches your head")
    print(game_over)


