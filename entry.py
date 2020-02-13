"""Built using freecodecamp.org tutorial at
https://www.youtube.com/watch?v=YXPyB4XeYLA
"""

from tkinter import *


def my_click():
    hello = "Hello " + e.get()
    my_label = Label(root, text=hello)
    my_label.pack()


root = Tk()

# Create and add Entry widget
e = Entry(root, width=50, borderwidth=5)
e.pack()

# Give e a default value
e.insert(0, "Enter Your Name")


# Create Button widget
my_button = Button(
    root,
    text="Enter Your Name",
    padx=50,
    pady=10,
    command=my_click,
    bg="green",
    fg="white"
)

# Add Button widget to screen
my_button.pack()

root.mainloop()