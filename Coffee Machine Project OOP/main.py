from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    is_on = True
    # Define the menu, coffee machine, and Money machine
    register = MoneyMachine()
    machine = CoffeeMaker()
    menu = Menu()
    while is_on:
        choice = ""
        # retrieve available menu items then prompt for user choice
        # Ensuring user doesn't input any blank text
        available_items = menu.get_items()
        while choice == "":
            choice = input(f"What would you like, {available_items}: ")
            if choice == "":
                print("Please enter something.")

        if choice == "report":
            machine.report()
            register.report()
        elif choice == "off":
            is_on = False
        else:
            # putting the item in a variable if it's available
            item = menu.find_drink(choice)
            # checking if there are resources to make drink
            if machine.is_resource_sufficient(item) and register.make_payment(item.cost):
                machine.make_coffee(item)


main()
