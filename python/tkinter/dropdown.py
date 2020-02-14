from tkinter import *
from PIL import ImageTk, Image  # Non-standard library `Pillow`


def show_selection():
    lbl = Label(root, text=selected.get())
    lbl.pack()

# Create root with title and favicon
root = Tk()
root.title("Sliders Exercise")
root.iconbitmap("images/favicon.ico")
root.geometry("400x400")

# Options for OptionMenu
options = [
    "Monday",
    "Tuesday", 
    "Wednesday",
    "Thursday",
    "Friday",
]

# StringVar to hold selected option, default = "Friday"
selected = StringVar()
selected.set(options[4])

# Add dropdown OptionMenu. Note: need to use asterisk if passing in list of 
# args for options. Otherwise just multiple comma separated values. e.g.:
# drop = OptionMenu(root, selected, "Monday", "Tuesday", "Wednesday")
drop = OptionMenu(root, selected, *options) 
drop.pack()

# Button
btn = Button(root, text="Show Selection", command=show_selection)
btn.pack()

# Main loop
root.mainloop()