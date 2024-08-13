# import tkinter
# Using this standard import statement, you must call every method by the Class name
# Ex. button = tkinter.button()
# This way avoids the redundant typing, only use this if you're only using one class
from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# There are three layout managers in tkinter, pack, place, and grid
# pack just throws it in a vertical order on the screen
# place allows you to place it in precise x and y coordinates
# Grid divides up the screen into columns and rows, allowing you to place different
# widgets on the screen relative to the  placed history
# creating a window just using the word, no tkinter.Tk(). just Tk()
window = Tk()
window.title("First program")
window.minsize(width=500, height=300)

# addding padding, adds space between the edge of the program and the window
window.config(padx=20, pady=20)

# Creating a label
my_label = Label(text="I am a label", font=("Times New Roman", 20))
# Editing the text and padding (space around widgets)
my_label.config(text="New Text", pady=5, padx=10)
# Grid adds the widget to the grid layout of my choice
my_label.grid(column=0, row=0)

# Button
my_button = Button(text="Click me", command=button_clicked)
my_button.grid(column=1, row=1)

# Button 2
my_button_2 = Button(text="Second button", command=button_clicked)
my_button_2.grid(column=2, row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

mainloop()
