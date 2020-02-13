from tkinter import *
from PIL import ImageTk, Image # Non-standard library `Pillow`


def open():
    global my_img

    # Create new top level window
    top = Toplevel()
    top.title("Second Window")
    top.iconbitmap("images/favicon.ico")
    my_img = ImageTk.PhotoImage(Image.open("images/duck.jpg"))
    my_label = Label(top, image=my_img)
    my_label.pack()

    # Add button to close window
    b_2 = Button(top, text="Close Window", command=top.destroy)
    b_2.pack()

# Create root with title and favicon
root = Tk()
root.title("Radio Buttons Exercise")
root.iconbitmap("images/favicon.ico")

b = Button(root, text="Open Second Window", command=open)
b.pack()

# Main loop
root.mainloop()