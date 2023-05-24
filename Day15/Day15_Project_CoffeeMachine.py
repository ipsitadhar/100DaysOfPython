from main import *

money = 0


def return_resource_value():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    resource_remaining = [water, milk, coffee]
    return resource_remaining


def print_report():
    # resource=return_resource_value()
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}ml")
    print(f"Money: ${money}")


def check_resources_sufficient(drink_name):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]


def make_coffee():
    user_choice = ""
    while user_choice != "off":
        user_choice = input("What would you like? (espresso/latte/cappuccino):")
        if user_choice == "report":
            print_report()


make_coffee()
