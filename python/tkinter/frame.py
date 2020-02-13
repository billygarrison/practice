from tkinter import *
from PIL import ImageTk, Image # Non-standard library `Pillow`

# Create root with title and favicon
root = Tk()
root.title("Frames Exercise")
root.iconbitmap("images/favicon.ico")

# Add frame to root
frame = LabelFrame(root, padx=20, pady=20)
frame.pack(padx=50, pady=50)

# Add buttons to frame
b_1 = Button(frame, text="Don't Click Here!", command=root.quit)
b_2 = Button(frame, text="...or here!", command=root.quit)
b_1.grid(row=0, column=0, padx=10)
b_2.grid(row=1, column=1, padx=10)

# Main loop
root.mainloop()