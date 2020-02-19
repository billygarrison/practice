"""Built using Codemy.com playlist videos 28-35
https://www.youtube.com/watch?
v=_RLq1jfapcA&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=28
"""


from tkinter import *
from PIL import ImageTk, Image
import sqlite3


def clear_fields():
    box_first_name.delete(0, END)
    box_last_name.delete(0, END)
    box_address1.delete(0, END)
    box_address2.delete(0, END)
    box_city.delete(0, END)
    box_state.delete(0, END)
    box_zipcode.delete(0, END)
    box_country.delete(0, END)
    box_phone.delete(0, END)
    box_email.delete(0, END)
    box_username.delete(0, END)
    box_payment_method.delete(0, END)
    box_discount_code.delete(0, END)
    box_price_paid.delete(0, END)


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
box_address1 = Entry(root)
box_address2 = Entry(root)
box_city = Entry(root)
box_state = Entry(root)
box_zipcode = Entry(root)
box_country = Entry(root)
box_phone = Entry(root)
box_email = Entry(root)
box_username = Entry(root)
box_payment_method = Entry(root)
box_discount_code = Entry(root)
box_price_paid = Entry(root)

# Add entrys to screen
box_first_name.grid(row=1, column=1, pady=5)
box_last_name.grid(row=2, column=1, pady=5)
box_address1.grid(row=3, column=1, pady=5)
box_address2.grid(row=4, column=1, pady=5)
box_city.grid(row=5, column=1, pady=5)
box_state.grid(row=6, column=1, pady=5)
box_zipcode.grid(row=7, column=1, pady=5)
box_country.grid(row=8, column=1, pady=5)
box_phone.grid(row=9, column=1, pady=5)
box_email.grid(row=10, column=1, pady=5)
box_username.grid(row=11, column=1, pady=5)
box_payment_method.grid(row=12, column=1, pady=5)
box_discount_code.grid(row=13, column=1, pady=5)
box_price_paid.grid(row=14, column=1, pady=5)

# Buttons
btn_add_customer = Button(root, text="Add Customer To Database")
btn_clear_fields = Button(root, text="Clear Fields", command=clear_fields)
btn_add_customer.grid(row=15, column=0, columnspan=2, padx=10, pady=10)
btn_clear_fields.grid(row=16, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
