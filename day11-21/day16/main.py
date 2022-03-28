from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

running = True

while running == True:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee == 'off':
        running = False
    elif coffee == 'report':
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(coffee) != None:
        coffee = menu.find_drink(coffee)
        if coffee_maker.is_resource_sufficient(coffee):
            if money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)
    else:
        pass


