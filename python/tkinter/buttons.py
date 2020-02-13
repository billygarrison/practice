"""Built using freecodecamp.org tutorial at
https://www.youtube.com/watch?v=YXPyB4XeYLA
"""

from tkinter import *


def my_click():
    my_label = Label(root, text="Look! I clicked a Button!")
    my_label.pack()


root = Tk()

# Create Button widget
my_button = Button(
    root,
    text="Click Me!",
    padx=50,
    pady=10,
    command=my_click,
    bg="green",
    fg="white"
)

# Add Button widget to screen
my_button.pack()

root.mainloop()