from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import string


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Creates a random password with a length 8-16
# At least one capital letter, one number, and one special character

def generate_password():
    password = []
    pass_length = random.randint(8, 16)
    special_characters_count = random.randint(1, 3)
    digits_count = random.randint(1, 3)

    password.append(random.choice(string.ascii_uppercase))
    for i in range(special_characters_count):
        password.append(random.choice(string.punctuation))
    for i in range(digits_count):
        password.append(random.choice(string.digits))
    for i in range(pass_length - len(password)):
        password.append(random.choice(string.ascii_letters))

    random.shuffle(password)
    password = ''.join(password)
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# program a command to the "add" button to save the information from
# all the entries into a file called data.txt with readable formatting

def save():
    user = username_entry.get()
    password = password_entry.get()
    website = website_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty Text", message="Please enter a website and password to be able to save!")

    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {user}\n"
                                                                f"Password:{password}"
                                                                f"\nIs it okay to save?")
        if is_okay:
            with open('data.txt', 'a') as file:
                file.write(f"{website} | {user} | {password}\n")
                password_entry.delete(0, END)
                website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

# creating the canvas and adding the logo
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Creating  labels and their respective buttons/entries entry boxes
# Website label and entry
website_label = Label(text="Website:")
website_entry = Entry(width=35)
# starts program with the cursor in this field
website_entry.focus()
website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
# Email/Username label and entry
username_label = Label(text="Email/Username:")
username_entry = Entry(width=35)
# adds a default email/username upon opening of the app
username_entry.insert(0, "aby2004.im@gmail.com")
username_label.grid(column=0, row=2)
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
# Password label and entry
password_label = Label(text="Password:")
password_entry = Entry(width=21)
password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3, columnspan=2, sticky="EW")
# Generate Password button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")
# Add button, The sticky kwargg is used to align the entries and/or buttons
add_info_button = Button(text="Add", width=35, command=save)
add_info_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
