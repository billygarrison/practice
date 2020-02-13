"""Built using freecodecamp.org tutorial at
https://www.youtube.com/watch?v=YXPyB4XeYLA
"""

from tkinter import *

# This has to go first in any tkinter program
root = Tk()

# Two steps to add anything in tkinter - define and add to screen
my_label = Label(root, text="Hello World!")
my_label.pack()

root.mainloop()