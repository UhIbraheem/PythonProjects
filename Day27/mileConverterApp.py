from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=10, pady=10)


# Creating button functionality
def mile_to_km():
    print("I got clicked")
    km_conversion = round(int(mile_input.get()) * 2.2)
    km_value.config(text=km_conversion)


Miles = Label(text="Miles", font=("Times New Roman", 14))
is_equal_to = Label(text="is equal to", font=("Times New Roman", 14))
Km = Label(text="Km", font=("Times New Roman", 14))
Miles.grid(column=2, row=0)
is_equal_to.grid(column=0, row=1)
Km.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)

mile_input = Entry(width=10)
mile_input.grid(column=1, row=0)

km_value = Label(text=0, font=("Times New Roman", 20))
km_value.grid(column=1, row=1)

mainloop()
