"""Built using Codemy.com playlist videos 28-35
https://www.youtube.com/watch?
v=_RLq1jfapcA&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=28
"""

import csv
from tkinter import *
#from tkinter import ttk
import sqlite3

from PIL import ImageTk, Image


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
    box_payment_method.delete(0, END)
    box_discount_code.delete(0, END)
    box_price_paid.delete(0, END)


def add_customer():
    sql_command = (
        "INSERT INTO customers ("
        + "first_name, last_name, zipcode, price_paid, email, "
        + "address_1, address_2, city, state, country, phone, "
        + "payment_method, discount_code"
        + ") "
        + " VALUES ("
        + ":first_name, :last_name, :zipcode, :price_paid, :email, "
        + ":address_1, :address_2, :city, :state, :country, :phone, "
        + ":payment_method, :discount_code"
        + ")"
    )

    values = {
        "first_name": box_first_name.get(),
        "last_name": box_last_name.get(),
        "zipcode": box_zipcode.get(),
        "price_paid": box_price_paid.get(),
        "email": box_email.get(),
        "address_1": box_address1.get(),
        "address_2": box_address2.get(),
        "city": box_city.get(),
        "state": box_state.get(),
        "country": box_country.get(),
        "phone": box_phone.get(),
        "payment_method": box_payment_method.get(),
        "discount_code": box_discount_code.get()
    }

    c.execute(sql_command, values)

    # Commit changes
    conn.commit()

    # Clear the boxes
    clear_fields()


def list_customers():
    # New window
    tk_list_customer = Tk()
    tk_list_customer.title("List All Customers")
    tk_list_customer.iconbitmap("../images/favicon.ico")
    tk_list_customer.geometry("900x600")

    # Query the database
    c.execute("SELECT * FROM customers")
    recs = c.fetchall()
    for i, rec in enumerate(recs):
        col_num = 0
        for cell_value in rec:
            lbl_lookup = Label(tk_list_customer, text=cell_value)
            lbl_lookup.grid(row=i, column=col_num)
            col_num += 1

    # Export to CSV button
    btn_csv = Button(tk_list_customer, text="Save As CSV", command=lambda: write_to_csv(recs))
    row_num = len(recs) + 1
    btn_csv.grid(row=row_num, column=0, padx=10, pady=10)


def search_customers():
    global box_search
    global tk_search_customers

    tk_search_customers = Tk()
    tk_search_customers.title("Search Customers")
    tk_search_customers.iconbitmap("../images/favicon.ico")
    tk_search_customers.geometry("900x600")

    # Create entry, label, and button for customer name to search
    lbl_search = Label(tk_search_customers, text="Search Customer By Last Name")
    box_search = Entry(tk_search_customers)
    btn_search = Button(tk_search_customers, text="Search Customers", command=search_by_last_name)
    lbl_search.grid(row=0, column=0, padx=10, pady=10)
    box_search.grid(row=0, column=1, padx=10, pady=10)
    btn_search.grid(row=1, column=0, padx=10, pady=10)


def search_by_last_name():
    global box_search
    global tk_search_customers

    search_name = box_search.get()
    sql = "SELECT * FROM customers WHERE last_name LIKE '" + search_name + "'"
    c.execute(sql)
    result = c.fetchall()

    if not result:
        result = "Record Not Found..."

    lbl_searched = Label(tk_search_customers, text=result)
    lbl_searched.grid(row=2, column=0, padx=10, pady=10, columnspan=2)


def write_to_csv(recs):
    with open("../data/customers.csv", "w+", newline="") as f:
        for rec in recs:
            csv_writer = csv.writer(f, dialect="excel")
            csv_writer.writerow(rec)


root = Tk()
root.title("CRM Tool")
root.iconbitmap("../images/favicon.ico")
root.geometry("400x800")

conn = sqlite3.connect("../data/crm.db")
c = conn.cursor()

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
box_payment_method.grid(row=12, column=1, pady=5)
box_discount_code.grid(row=13, column=1, pady=5)
box_price_paid.grid(row=14, column=1, pady=5)

# Create buttons
btn_add_customer = Button(
    root,
    text="Add Customer To Database",
    command=add_customer
)
btn_clear_fields = Button(root, text="Clear Fields", command=clear_fields)
btn_list_customers = Button(root, text="List Customers", command=list_customers)
btn_search_customers = Button(root, text="Search Customers", command=search_customers)

# Add buttons to screen
btn_add_customer.grid(row=15, column=0, columnspan=2, padx=10, pady=10)
btn_clear_fields.grid(row=16, column=0, columnspan=2, padx=10, pady=10)
btn_list_customers.grid(row=17, column=0, columnspan=2, padx=10, pady=10)
btn_search_customers.grid(row=18, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()

conn.close()