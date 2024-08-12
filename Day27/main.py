# import tkinter
# Using this standard import statement, you must call every method by the Class name
# Ex. button = tkinter.button()
# This way avoids the redundant typing, only use this if you're only using one class
from tkinter import *

# creating a window just using the word, no tkinter.Tk(). just Tk()
window = Tk()
window.title("First program")
window.minsize(width=500, height=300)


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# Creating a label
my_label = Label(text="I am a label", font=("Times New Roman", 20))
# Editing the text
my_label.config(text="New Text")
# Packing the label sends it to the window
my_label.pack()

# Button
my_button = Button(text="Click me", command=button_clicked)
my_button.pack()

# Entry
input = Entry(width= 10)
print(input.get())
input.pack()

mainloop()
