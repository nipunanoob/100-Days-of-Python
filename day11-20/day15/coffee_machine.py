MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

running = True


def generate_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def insert_coins():
    inserted_value = 0
    coins = {'quarters': {'value': 0.25, 'inserted': 0},
             'dimes': {'value': 0.1, 'inserted': 0},
             'nickles': {'value': 0.05, 'inserted': 0},
             'pennies': {'value': 0.01, 'inserted': 0}}
    values = [0.25, 0.1, 0.05, 0.01]
    for key in coins:
        coins[key]['inserted'] = int(input(f"how many {key}: "))
        inserted_value += coins[key]['inserted'] * coins[key]['value']
    inserted_value = round(inserted_value, 2)
    print(inserted_value)
    if inserted_value < option['cost']:
        print("Sorry that's not enough coins...Refunding...")
        return 0
    return inserted_value


while running:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee == 'off':
        running = False
    elif coffee == 'report':
        generate_report()
    elif coffee in ['espresso', 'latte', 'cappuccino']:
        available = True
        option = MENU[coffee]
        for item, ingredient in option['ingredients'].items():
            if ingredient > resources[item]:
                print(f"Sorry we do not have enough {item}")
                available = False
                break
        if available:
            print("Please, insert coins.")
            user_amount = insert_coins()
            if not user_amount:
                continue
            else:
                change = user_amount - option['cost']
                print(f"Here is ${change} in change")
                print("Here is your espresso ☕. Enjoy")
                resources["money"] += option['cost']
                for item, ingredient in option['ingredients'].items():
                    if item != 'money':
                        resources[item] -= ingredient

    else:
        print("Invalid input!")
