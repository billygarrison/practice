"""Built using freecodecamp.org tutorial at
https://www.youtube.com/watch?v=YXPyB4XeYLA
"""

from tkinter import *

# This has to go first in any tkinter program
root = Tk()

# Create Label widgets
my_label1 = Label(root, text="Hello World!")
my_label2 = Label(root, text="My name is Billy Garrison")

# Put both Labels on screen using grid (row and column numbers are relative)
my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=5)

root.mainloop()