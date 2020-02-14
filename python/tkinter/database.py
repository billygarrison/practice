from tkinter import *
from PIL import ImageTk, Image  # Non-standard library `Pillow`
import sqlite3

# Create root with title and favicon
root = Tk()
root.title("Sliders Exercise")
root.iconbitmap("images/favicon.ico")
root.geometry("400x400")

# Create a database or connect to one
conn = sqlite3.connect("data/address_book.db")

# Create cursor
c = conn.cursor()

# Create table
c.execute(
    "CREATE TABLE addresses ("
    + "first_name text, "
    + "last_name text, "
    + "address text, "
    + "city text, "
    + "state text, "
    + "zipcode integer"
    + ")"
)

# Commit changes
conn.commit()

# Close connection
conn.close()

# Main loop
root.mainloop()