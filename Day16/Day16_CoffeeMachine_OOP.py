from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
menu = Menu()
machine = MoneyMachine()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report()
        machine.report()
    else:
        drink = menu.find_drink(choice)
        if machine.make_payment(drink.cost) and coffee.is_resource_sufficient(drink):
            coffee.make_coffee(drink)

