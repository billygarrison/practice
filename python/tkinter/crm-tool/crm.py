"""Built using Codemy.com playlist videos 28-35
https://www.youtube.com/watch?
v=_RLq1jfapcA&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=28
"""

from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("CRM Tool")
root.iconbitmap("../images/favicon.ico")
root.geometry("400x600")

# Title label
lbl_title = Label(root, text="Customer Database", font=("Helvetica", 16))
lbl_title.grid(row=0, column=0, columnspan=2, pady=10)

# Labels for main form to enter customer data
lbl_first_name = Label(root, text="First Name")
lbl_last_name = Label(root, text="Last Name")
lbl_address1 = Label(root, text="Address 1")
lbl_address2 = Label(root, text="Address2")
lbl_city = Label(root, text="City")
lbl_state = Label(root, text="State")
lbl_zipcode = Label(root, text="Zip Code")
lbl_country = Label(root, text="Country")
lbl_phone = Label(root, text="Phone Number")
lbl_email = Label(root, text="Email Address")
lbl_username = Label(root, text="Username")
lbl_payment_method = Label(root, text="Payment Method")
lbl_discount_code = Label(root, text="Discount Code")
lbl_price_paid = Label(root, text="Price Paid")

# Add labels to screen
lbl_first_name.grid(row=1, column=0, sticky="w", padx=10)
lbl_last_name.grid(row=2, column=0, sticky="w", padx=10)
lbl_address1.grid(row=3, column=0, sticky="w", padx=10)
lbl_address2.grid(row=4, column=0, sticky="w", padx=10)
lbl_city.grid(row=5, column=0, sticky="w", padx=10)
lbl_state.grid(row=6, column=0, sticky="w", padx=10)
lbl_zipcode.grid(row=7, column=0, sticky="w", padx=10)
lbl_country.grid(row=8, column=0, sticky="w", padx=10)
lbl_phone.grid(row=9, column=0, sticky="w", padx=10)
lbl_email.grid(row=10, column=0, sticky="w", padx=10)
lbl_username.grid(row=11, column=0, sticky="w", padx=10)
lbl_payment_method.grid(row=12, column=0, sticky="w", padx=10)
lbl_discount_code.grid(row=13, column=0, sticky="w", padx=10)
lbl_price_paid.grid(row=14, column=0, sticky="w", padx=10)

# Entrys for main form to enter customer data
box_first_name = Entry(root)
box_last_name = Entry(root)
lbl_address1 = Entry(root)
lbl_address2 = Entry(root)
lbl_city = Entry(root)
lbl_state = Entry(root)
lbl_zipcode = Entry(root)
lbl_country = Entry(root)
lbl_phone = Entry(root)
lbl_email = Entry(root)
lbl_username = Entry(root)
lbl_payment_method = Entry(root)
lbl_discount_code = Entry(root)
lbl_price_paid = Entry(root)

# Add entrys to screen
box_first_name.grid(row=1, column=1, pady=5)
box_last_name.grid(row=2, column=1, pady=5)
lbl_address1.grid(row=3, column=1, pady=5)
lbl_address2.grid(row=4, column=1, pady=5)
lbl_city.grid(row=5, column=1, pady=5)
lbl_state.grid(row=6, column=1, pady=5)
lbl_zipcode.grid(row=7, column=1, pady=5)
lbl_country.grid(row=8, column=1, pady=5)
lbl_phone.grid(row=9, column=1, pady=5)
lbl_email.grid(row=10, column=1, pady=5)
lbl_username.grid(row=11, column=1, pady=5)
lbl_payment_method.grid(row=12, column=1, pady=5)
lbl_discount_code.grid(row=13, column=1, pady=5)
lbl_price_paid.grid(row=14, column=1, pady=5)

root.mainloop()
