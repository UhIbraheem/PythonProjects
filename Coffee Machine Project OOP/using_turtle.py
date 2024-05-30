# This window will be turtle library usage
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.color("cyan4")
# timmy.shape("turtle")
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()

# working with pretty table
from prettytable import PrettyTable

table = PrettyTable()

# adding a column to table
table.add_column("Pokemon", ["Squirtle", "Charmander", "Pickachu"])
table.add_column("Type", ["Water", "Fire", "Electric"])

table.align = "l"

print(table)
