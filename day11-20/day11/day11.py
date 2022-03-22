import random
import day11art
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

def show_player_cards():
    print(f"Your cards: {player}, current score: {player_value}")
    print(f"Dealer has drawn {dealer[0]} as his first card")

def bust(name):
    print(f"{name} has busted")

def blackjack(name):
    print(f"{name} got blackjack")



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
logo = day11art.logo

while(True):
    option = ""
    game = input("Do you want to play a round of blackjack? Type 'y' or 'n': ")
    if game =='n':
        print("Ok, Goodbye!")
        break
    elif game == 'y':
        print(logo)
        player = []
        dealer = []
        for i in range(2):
            player.append(cards[random.randint(0,12)])
            dealer.append(cards[random.randint(0,12)])
        player_value = sum(player)
        dealer_value = sum(dealer)
        if player_value == 22:
            player[0] = 1
        if dealer_value == 22:
            dealer[0] == 1
        show_player_cards()
        while(option != 'stay'):
            option = input("Type 'hit' to draw more cards or 'stay' to stop drawing: ")
            if option == 'hit':
                card = random.randint(0,12)
                print(f"You have drawn {cards[card]}")
                player.append(cards[card])
                player_value = sum(player)
                if player_value == 21:
                    show_player_cards()
                    blackjack("You")
                    break
                elif player_value > 21:
                    if 11 in player:
                        card = player.index(11)
                        player[card] = 1
                        player_value = sum(player)
                        if 11 in player and player_value > 21:
                            card = player.index(11)
                            player[card] = 1
                        elif player_value > 21:
                            show_player_cards()
                            bust("You")
                            print("You lose!")
                            break
                        else:
                            pass
                        player_value = sum(player)
                        show_player_cards()
                    else:
                        show_player_cards()
                        bust("You")
                        print("You lose!")
                        break
                else:
                    show_player_cards()
            elif option == 'stay':
                pass
            else:
                print("Invalid option!")
        if option == 'stay' or player_value == 21:
            print(f"Dealer reveals the hidden card, it is {dealer[1]}")
            while dealer_value < 17:
                card = cards[random.randint(0,12)]
                dealer.append(card)
                print(f"Dealer has drawn {card}")
                dealer_value = sum(dealer)
                if dealer_value == 21:
                    blackjack("Dealer")
                elif dealer_value > 21:
                    bust("Dealer")
                    continue
                else:
                    pass
            print(f"Your final cards: {player}, current score: {player_value}")
            print(f"Dealer's cards: {dealer}, current score: {dealer_value}")
            if player_value == dealer_value:
                print(f"You tie!")
            elif player_value < dealer_value and dealer_value <=21:
                print(f"You lose!")
            else:
                print(f"You win!")

    else:
        print("You entered an invalid option!")





