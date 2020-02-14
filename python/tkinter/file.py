from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image # Non-standard library `Pillow`


def open():
    global my_image

    # Get file name from dialog
    root.filename = filedialog.askopenfilename(
        initialdir="C:/Users/garrisow/Desktop/practice/python/tkinter",
        title="Select A File",
        filetypes=(
            ("jpg files", "*.jpg"),
            ("png files", "*.png"),
            ("all files", "*.*")
        )
    )

    # Display file path and image
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


# Create root with title and favicon
root = Tk()
root.title("File Open Exercise")
root.iconbitmap("images/favicon.ico")

b = Button(root, text="Open File", command=open).pack()

# Main loop
root.mainloop()