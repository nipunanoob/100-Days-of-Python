import day9_art
import os

logo = day9_art.logo
flag = True
print(logo)

auction_dict = {}

while(flag):
    name = input("Enter name of bidder: ")
    price = int(input("Enter bid price: "))
    auction_dict[name] = price
    option = input("Are there any more bidders for this auction? Type yes/no: ").lower()
    if option == 'no':
        flag = False
    os.system('cls')

max = 0
for key in auction_dict:
    if auction_dict[key] > max:
        max = auction_dict[key]
        winner = key

print(f"{winner.strip().capitalize()} has won the auction with ${max} bid")