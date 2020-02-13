from tkinter import *
from PIL import ImageTk, Image # Non-standard library `Pillow`


def back(image_number):
    global my_label
    global button_back
    global button_forward
    global status

    # Remove old image and update with new image
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])

    # Update back and forward buttons
    button_back = Button(
        root,
        text="<<",
        command=lambda: back(image_number - 1)
    )
    button_forward = Button(
        root,
        text=">>",
        command=lambda: forward(image_number + 1)
    )
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Update status bar
    status = Label(
        root,
        text="Image " + str(image_number) + " of " + str(len(image_list)),
        bd=1,
        relief=SUNKEN,
        anchor=E
    )
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def forward(image_number):
    global my_label
    global button_back
    global button_forward
    global status

    # Remove old image and update with new image
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])

    # Update back and forward buttons
    button_back = Button(
        root,
        text="<<",
        command=lambda: back(image_number - 1)
    )
    button_forward = Button(
        root,
        text=">>",
        command=lambda: forward(image_number + 1)
    )
    if image_number == len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Update status bar
    status = Label(
        root,
        text="Image " + str(image_number) + " of " + str(len(image_list)),
        bd=1,
        relief=SUNKEN,
        anchor=E
    )
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# Create root with title and favicon
root = Tk()
root.title("Images Exercise")
root.iconbitmap("images/favicon.ico")

# Create images and add them to list
my_img_1 = ImageTk.PhotoImage(Image.open("images/vfpicon_full.png"))
my_img_2 = ImageTk.PhotoImage(Image.open("images/duck.jpg"))
image_list = [my_img_1, my_img_2]

# Status bar
status = Label(
    root,
    text="Image 1 of " + str(len(image_list)),
    bd=1,
    relief=SUNKEN,
    anchor=E
)

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
button_forward.grid(row=1, column=2, pady=10)

# Add status bar to root
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# Main loop
root.mainloop()