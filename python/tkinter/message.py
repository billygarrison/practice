from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image # Non-standard library `Pillow`


# messagebox types:
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    response = messagebox.askyesno("Popup Title", "Hello world!")

    if response == 1:
        text = "You clicked yes!"
    else:
        text = "You clicked no!"

    response_label = Label(root, text=text)
    response_label.pack()

# Create root with title and favicon
root = Tk()
root.title("Radio Buttons Exercise")
root.iconbitmap("images/favicon.ico")

# Button
b = Button(root, text="Popup", command=popup)
b.pack()

# Main loop
root.mainloop()