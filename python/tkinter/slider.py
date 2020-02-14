from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image  # Non-standard library `Pillow`


def set_window_size():
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


# Create root with title and favicon
root = Tk()
root.title("Sliders Exercise")
root.iconbitmap("images/favicon.ico")

# Add vertical slider
vertical = Scale(root, from_=0, to=400)
vertical.pack()

# Add horizontal slider
horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

# Add button to get horizontal slider value
b = Button(root, text="Click Me!", command=set_window_size)
b.pack()

# Main loop
root.mainloop()