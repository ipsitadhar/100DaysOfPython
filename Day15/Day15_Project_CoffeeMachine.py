from main import *

money = 0
less_resource = False


def print_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def check_resources_sufficient(drink_name):
    global less_resource
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    water_required = MENU[drink_name]["ingredients"]["water"]
    coffee_required = MENU[drink_name]["ingredients"]["coffee"]
    if water_required > water:
        print("Sorry there is not enough water.")
        less_resource = True
    if drink_name != "espresso":
        milk_required = MENU[drink_name]["ingredients"]["milk"]
        if milk_required > milk:
            print("Sorry there is not enough milk.")
            less_resource = True
    if coffee_required > coffee:
        print("Sorry there is not enough coffee.")
        less_resource = True


def recalculate_resources(drink):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    water_used = MENU[drink]["ingredients"]["water"]
    coffee_used = MENU[drink]["ingredients"]["coffee"]
    resources["water"] = water - water_used
    if drink != "espresso":
        milk_used = MENU[drink]["ingredients"]["milk"]
        resources["milk"] = milk - milk_used
    resources["coffee"] = coffee - coffee_used


def process_coins():
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickles = int(input("How many nickles?:"))
    pennies = int(input("How many pennies?:"))
    total = .25 * quarters + .1 * dimes + .05 * nickles + .01 * pennies
    return total


def make_coffee():
    global money
    user_choice = ""
    while user_choice != "off":
        user_choice = input("What would you like? (espresso/latte/cappuccino):")
        if user_choice == "report":
            print_report()
        elif user_choice != "off":
            check_resources_sufficient(user_choice)
            if not less_resource:
                print("Please insert coins")
                total = process_coins()
                cost = MENU[user_choice]["cost"]
                if total < cost:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    return_amount = round(total - cost, 2)
                    money = money + cost
                    recalculate_resources(user_choice)
                    print(f"Here is ${return_amount} in change")
                    print(f"Here is your {user_choice} ☕ Enjoy")


make_coffee()
