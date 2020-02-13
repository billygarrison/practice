from tkinter import *
from PIL import ImageTk, Image # Non-standard library `Pillow`


def back(image_number):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def forward(image_number):
    global my_label
    global button_back
    global button_forward

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


# Create root with title and favicon
root = Tk()
root.title("Images Exercise")
root.iconbitmap("images/favicon.ico")

# Create images and add them to list
my_img_1 = ImageTk.PhotoImage(Image.open("images/vfpicon_full.png"))
my_img_2 = ImageTk.PhotoImage(Image.open("images/duck.jpg"))
image_list = [my_img_1, my_img_2]

# Create Label for initial image
my_label = Label(image=my_img_1)
my_label.grid(row=0, column=0, columnspan=3)

# Create back, forward, and quit buttons
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_forward = Button(root, text=">>", command=lambda: forward(2))
button_quit = Button(root, text="Exit Program", command=root.quit)

# Add buttons to root
button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

# Main loop
root.mainloop()