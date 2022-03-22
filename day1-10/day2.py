print("Welcome to the tip calculator")
print("What was the total bill? $",end="")
total = float(input())
print("How many people to split the bill with?",end=" ")
num_people = int(input())
while(True):
    print("What percentage tip would you like to give? 10, 12 or 15",end=" ")
    tip_perc = int(input())
    if tip_perc in [10,12,15]:
        break
    print("Invalid tip")
owed_amount = round((total + (total * tip_perc) / 100 ) / num_people, 1)
print("Each person should pay: $"+str(owed_amount))

      
