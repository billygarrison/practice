from tkinter import *
from PIL import ImageTk, Image # Non-standard library `Pillow`


def click(value):
    # Update label
    my_label = Label(root, text=value)
    my_label.pack()


# Create root with title and favicon
root = Tk()
root.title("Radio Buttons Exercise")
root.iconbitmap("images/favicon.ico")

# Radiobutton modes
TOPPINGS = [
    ("Cheddar", "Cheddar"),
    ("Mozzarella", "Mozzarella"),
    ("Monterey Jack", "Monterey Jack"),
    ("Feta", "Feta"),
]

# pizza variable
pizza = StringVar()
pizza.set("Mozzarella")

# Add a Radiobutton for each mode in TOPPINGS
for text, topping in TOPPINGS:
    r = Radiobutton(root, text=text, variable=pizza, value=topping)
    r.pack(anchor=W)

# Button to add label with radio button value
my_button = Button(root, text="Click Me!", command=lambda: click(pizza.get()))
my_button.pack()

# Main loop
root.mainloop()