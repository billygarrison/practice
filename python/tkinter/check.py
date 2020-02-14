from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image  # Non-standard library `Pillow`


def show_chk_value():
    global my_label
    my_label = Label(root, text=check_variable.get())
    my_label.pack()


# Create root with title and favicon
root = Tk()
root.title("Sliders Exercise")
root.iconbitmap("images/favicon.ico")
root.geometry("400x400")

# Add check box
check_variable = StringVar()
chk = Checkbutton(
    root,
    text="Check this box, I dare you!",
    onvalue="on",
    offvalue="off",
    variable=check_variable
)
chk.deselect()  # Deselect to workaround bug
chk.pack()

# Add button to display check value
btn = Button(
    root,
    text="Show Selection",
    command=show_chk_value
)
btn.pack()

# Main loop
root.mainloop()