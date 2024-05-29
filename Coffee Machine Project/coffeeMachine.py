# This project will make a coffe machine for office workers
# The workers can order by choosing from the list of options,
# The coffee machine also checks the amount of ingredients available to be used
# Then it requests coins to be inserted as payment
# The machine stores the amount of money and subtracts any ingredients used
# Then it repeats this cycle until it's out of ingredients

# First, import the data from the local file
from coffeeMachineData import MENU, resources


# Function 1
# Prompt user for input and store their choice in a userChoice variable
def drink_choice():
    choice = ""
    options = ["off", "report", "espresso", "latte", "cappuccino"]
    while choice not in options:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice not in options:
            print("Please enter espresso/latte/cappuccino!")
    return choice


# Function 2
# Checks for resources before making the desired drink
def enough_resources(drink):
    water = coffee = milk = False
    if drink == "espresso":
        if MENU[drink]["ingredients"]["water"] < resources["water"]:
            water = True
        if MENU[drink]["ingredients"]["coffee"] < resources["coffee"]:
            coffee = True
        if coffee and water:
            return True
    else:
        if MENU[drink]["ingredients"]["water"] < resources["water"]:
            water = True
        if MENU[drink]["ingredients"]["coffee"] < resources["coffee"]:
            coffee = True
        if MENU[drink]["ingredients"]["milk"] < resources["milk"]:
            milk = True
        if coffee and water and milk:
            return True

    return False


# Function 3
# checks for enough money before dispensing the drink
def enough_money(drink):
    price = MENU[drink]["cost"]
    quarter, dime, nickel, penny = .25, .10, .05, .01

    print("Please insert coins.")
    quarters = int(input("Enter Quarters: "))
    dimes = int(input("Enter Dimes: "))
    nickels = int(input("Enter Nickels: "))
    pennies = int(input("Enter Pennies: "))

    userMoney = (quarters * quarter) + (dimes * dime) + (nickels * nickel) + (pennies * penny)
    if userMoney >= price:
        userMoney -= price
        resources["money"] += price
        if userMoney > 0:
            print(f"Here is your change, ${userMoney:.2f}")
        return True
    else:
        return False


def main():
    isOn = True
    while isOn:
        drink = drink_choice()
        if drink == "off":
            isOn = False
            print("Shutting down...")
            break
        elif drink == "report":
            print(resources)
        else:
            hasIngredients = enough_resources(drink)
            if hasIngredients:
                hasMoney = enough_money(drink)
                if hasMoney:
                    if drink == "espresso":
                        resources["water"] -= MENU[drink]["ingredients"]["water"]
                        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
                    else:
                        resources["water"] -= MENU[drink]["ingredients"]["water"]
                        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
                        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
                    print(f"Here is your {drink}!")
                else:
                    print("Insufficient funds!")
            else:
                print(f"The machine is out of ingredients to make a(n) {drink}!")


main()
