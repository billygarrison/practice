from tkinter import *
from PIL import ImageTk, Image # Non-standard library `Pillow`


root = Tk()
root.title("Images Exercise")
root.iconbitmap("images/favicon.ico")

# Can add images to almost any Tkinter widget
my_img = ImageTk.PhotoImage(Image.open("images/vfpicon_full.png"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()