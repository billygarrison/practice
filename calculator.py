"""Built using freecodecamp.org tutorial at
https://www.youtube.com/watch?v=YXPyB4XeYLA
"""

from tkinter import *

root = Tk()
root.title("Simple Calculator")

# Create Entry widget
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def num(number):
    # Append number to Entry's value
    e.insert(END, str(number))


def clr():
    e.delete(0, END)


def add():
    global first_number
    global math
    first_number = int(e.get())
    math = "add"
    e.delete(0, END)


def subtract():
    global first_number
    global math
    first_number = int(e.get())
    math = "subtract"
    e.delete(0, END)


def multiply():
    global first_number
    global math
    first_number = int(e.get())
    math = "multiply"
    e.delete(0, END)


def divide():
    global first_number
    global math
    first_number = int(e.get())
    math = "divide"
    e.delete(0, END)


def equal():
    second_number = int(e.get())
    e.delete(0, END)

    if math == "add":
        result = first_number + second_number
    elif math == "subtract":
        result = first_number - second_number
    elif math == "multiply":
        result = first_number * second_number
    elif math == "divide":
        if second_number is not 0:
            result = first_number / second_number
        else:
            result = "Can't divide by 0!"

    e.insert(0, result)


# Define number buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: num(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: num(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: num(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: num(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: num(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: num(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: num(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: num(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: num(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: num(0))

# Define function buttons
button_add = Button(root, text="+", padx=39, pady=20, command=add)
button_subtract = Button(root, text="-", padx=40.5, pady=20, command=subtract)
button_multiply = Button(root, text="*", padx=41, pady=20, command=multiply)
button_divide = Button(root, text="/", padx=39, pady=20, command=divide)
button_equal = Button(root, text="=", padx=87, pady=20, command=equal)
button_clear = Button(root, text="Clear", padx=77, pady=20, command=clr)

# Put the buttons on the screen (top row)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

# Put the buttons on the screen (middle row)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

# Put the buttons on the screen (bottom row)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

# Put the zero button on the screen
button_0.grid(row=4, column=0)

# Put the function buttons on the screen
button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

# Main tkinter loop
root.mainloop()