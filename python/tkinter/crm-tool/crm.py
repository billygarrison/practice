"""Built using Codemy.com playlist videos 28-38
https://www.youtube.com/watch?
v=_RLq1jfapcA&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=28
"""

import csv
from tkinter import *
from tkinter import filedialog
from tkinter import ttk  # Used for ComboBox
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
    # Create new window to list customers
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
    btn_csv = Button(
        tk_list_customer,
        text="Save As CSV",
        command=lambda: write_to_csv(recs)
    )
    row_num = len(recs) + 1
    btn_csv.grid(row=row_num, column=0, padx=10, pady=10)


def search_customers():
    global box_search
    global tk_search_customers
    global cbo_search

    # Create new window for customer search
    tk_search_customers = Tk()
    tk_search_customers.title("Search Customers")
    tk_search_customers.iconbitmap("../images/favicon.ico")
    tk_search_customers.geometry("1100x800")

    # Create entry, label, and button for customer name to search
    lbl_search = Label(tk_search_customers, text="Search Customer")
    box_search = Entry(tk_search_customers)
    btn_search = Button(
        tk_search_customers,
        text="Search Customers",
        command=search_by
    )
    lbl_search.grid(row=0, column=0, padx=10, pady=10)
    box_search.grid(row=0, column=1, padx=10, pady=10)
    btn_search.grid(row=1, column=0, padx=10, pady=10)

    # Search by ComboBox
    cbo_search = ttk.Combobox(tk_search_customers, value=[
        "Search by...",
        "Last Name",
        "Email Address",
        "Customer ID",
    ])
    cbo_search.current(1)  # Defaults to index-1 of the value list "Last Name"
    cbo_search.grid(row=0, column=2)


def search_by():
    global box_search
    global tk_search_customers
    global cbo_search

    # Get values from combo box and entry box
    cbo_search_selected = cbo_search.get()
    search_val = box_search.get()

    # SQL statement depends on combobox option
    if cbo_search_selected == "Last Name":
        sql = (
            "SELECT * FROM customers WHERE last_name LIKE '"
            + search_val + "'"
        )
    elif cbo_search_selected == "Email Address":
        sql = "SELECT * FROM customers WHERE email LIKE '" + search_val + "'"
    elif cbo_search_selected == "Customer ID":
        sql = "SELECT * FROM customers WHERE user_id = " + search_val

    # If the user selected an option from the combo box, look up results
    if cbo_search_selected != "Search by...":
        # Get records, display message if no records found
        c.execute(sql)
        recs = c.fetchall()
        if not recs:
            txt = "Record Not Found..."
            lbl_searched = Label(tk_search_customers, text=txt)
            lbl_searched.grid(row=3, column=0)
        else:
            # Enumerate through records
            for i, rec in enumerate(recs):
                col_num = 0
                id_reference = str(rec[4])

                # Add Edit button
                btn_edit = Button(
                    tk_search_customers,
                    text="Edit",
                    command=lambda id_reference=id_reference: edit_record(
                        id_reference,
                        i+7
                    )
                )
                btn_edit.grid(row=i + 2, column=col_num)

                # Loop through cells in record, adding them to screen
                for cell_value in rec:
                    lbl_searched = Label(tk_search_customers, text=cell_value)
                    row_num = i + 2
                    lbl_searched.grid(row=row_num, column=col_num + 1)
                    col_num += 1

            # Export to CSV button
            btn_csv = Button(
                tk_search_customers,
                text="Save As CSV",
                command=lambda: write_to_csv(recs)
            )
            row_num = len(recs) + 3
            btn_csv.grid(row=row_num, column=0, padx=10, pady=10)


def edit_record(id, start_row):
    global tk_search_customers
    global box_edit_first_name
    global box_edit_last_name
    global box_edit_address1
    global box_edit_address2
    global box_edit_city
    global box_edit_state
    global box_edit_zipcode
    global box_edit_country
    global box_edit_phone
    global box_edit_email
    global box_edit_payment_method
    global box_edit_discount_code
    global box_edit_price_paid
    global box_edit_id

    # Get record for this user id
    edit_sql = "SELECT * FROM customers WHERE user_id = " + id
    c.execute(edit_sql)
    edit_rec = c.fetchall()[0]

    # Labels for editing records to enter customer data
    lbl_edit_first_name = Label(tk_search_customers, text="First Name")
    lbl_edit_last_name = Label(tk_search_customers, text="Last Name")
    lbl_edit_address1 = Label(tk_search_customers, text="Address 1")
    lbl_edit_address2 = Label(tk_search_customers, text="Address 2")
    lbl_edit_city = Label(tk_search_customers, text="City")
    lbl_edit_state = Label(tk_search_customers, text="State")
    lbl_edit_zipcode = Label(tk_search_customers, text="Zip Code")
    lbl_edit_country = Label(tk_search_customers, text="Country")
    lbl_edit_phone = Label(tk_search_customers, text="Phone Number")
    lbl_edit_email = Label(tk_search_customers, text="Email Address")
    lbl_edit_payment_method = Label(tk_search_customers, text="Payment Method")
    lbl_edit_discount_code = Label(tk_search_customers, text="Discount Code")
    lbl_edit_price_paid = Label(tk_search_customers, text="Price Paid")

    # Add labels to screen
    lbl_edit_first_name.grid(row=start_row + 1, column=0, sticky="w", padx=10)
    lbl_edit_last_name.grid(row=start_row + 2, column=0, sticky="w", padx=10)
    lbl_edit_address1.grid(row=start_row + 3, column=0, sticky="w", padx=10)
    lbl_edit_address2.grid(row=start_row + 4, column=0, sticky="w", padx=10)
    lbl_edit_city.grid(row=start_row + 5, column=0, sticky="w", padx=10)
    lbl_edit_state.grid(row=start_row + 6, column=0, sticky="w", padx=10)
    lbl_edit_zipcode.grid(row=start_row + 7, column=0, sticky="w", padx=10)
    lbl_edit_country.grid(row=start_row + 8, column=0, sticky="w", padx=10)
    lbl_edit_phone.grid(row=start_row + 9, column=0, sticky="w", padx=10)
    lbl_edit_email.grid(row=start_row + 10, column=0, sticky="w", padx=10)
    lbl_edit_payment_method.grid(
        row=start_row + 12,
        column=0,
        sticky="w",
        padx=10
    )
    lbl_edit_discount_code.grid(
        row=start_row + 13,
        column=0,
        sticky="w",
        padx=10
    )
    lbl_edit_price_paid.grid(row=start_row + 14, column=0, sticky="w", padx=10)

    # Entrys for main form to enter customer data
    box_edit_first_name = Entry(tk_search_customers)
    box_edit_last_name = Entry(tk_search_customers)
    box_edit_address1 = Entry(tk_search_customers)
    box_edit_address2 = Entry(tk_search_customers)
    box_edit_city = Entry(tk_search_customers)
    box_edit_state = Entry(tk_search_customers)
    box_edit_zipcode = Entry(tk_search_customers)
    box_edit_country = Entry(tk_search_customers)
    box_edit_phone = Entry(tk_search_customers)
    box_edit_email = Entry(tk_search_customers)
    box_edit_payment_method = Entry(tk_search_customers)
    box_edit_discount_code = Entry(tk_search_customers)
    box_edit_price_paid = Entry(tk_search_customers)

    # Add entrys to screen
    box_edit_first_name.grid(row=start_row + 1, column=1, pady=5)
    box_edit_last_name.grid(row=start_row + 2, column=1, pady=5)
    box_edit_address1.grid(row=start_row + 3, column=1, pady=5)
    box_edit_address2.grid(row=start_row + 4, column=1, pady=5)
    box_edit_city.grid(row=start_row + 5, column=1, pady=5)
    box_edit_state.grid(row=start_row + 6, column=1, pady=5)
    box_edit_zipcode.grid(row=start_row + 7, column=1, pady=5)
    box_edit_country.grid(row=start_row + 8, column=1, pady=5)
    box_edit_phone.grid(row=start_row + 9, column=1, pady=5)
    box_edit_email.grid(row=start_row + 10, column=1, pady=5)
    box_edit_payment_method.grid(row=start_row + 12, column=1, pady=5)
    box_edit_discount_code.grid(row=start_row + 13, column=1, pady=5)
    box_edit_price_paid.grid(row=start_row + 14, column=1, pady=5)

    # Fill entrys with existing values
    box_edit_first_name.insert(0, edit_rec[0])
    box_edit_last_name.insert(0, edit_rec[1])
    box_edit_address1.insert(0, edit_rec[6])
    box_edit_address2.insert(0, edit_rec[7])
    box_edit_city.insert(0, edit_rec[8])
    box_edit_state.insert(0, edit_rec[9])
    box_edit_zipcode.insert(0, edit_rec[2])
    box_edit_country.insert(0, edit_rec[10])
    box_edit_phone.insert(0, edit_rec[11])
    box_edit_email.insert(0, edit_rec[5])
    box_edit_payment_method.insert(0, edit_rec[12])
    box_edit_discount_code.insert(0, edit_rec[13])
    box_edit_price_paid.insert(0, edit_rec[3])

    # Save changes button
    btn_edit_save = Button(
        tk_search_customers,
        text="Save Changes",
        command=save_changes
    )
    btn_edit_save.grid(row=start_row + 16, column=0, padx=10, pady=10)


def save_changes():
    global box_edit_id

    # Get ID to edit
    id_to_edit = box_edit_id.get()

    # SQL command to update record for this user ID
    sql_command = (
        "UPDATE customers SET "
        + "first_name = ? , "
        + "last_name = ? , "
        + "address_1 = ? , "
        + "address_2 = ? , "
        + "city = ? , "
        + "state = ? , "
        + "zipcode = ? , "
        + "country = ? , "
        + "phone = ? , "
        + "email = ? , "
        + "payment_method = ? , "
        + "discount_code = ? , "
        + "price_paid = ? "
        + "WHERE user_id = ?"
    )

    # Get updated values from Entry boxes for sql command
    first_name = box_edit_first_name.get()
    last_name = box_edit_last_name.get()
    address_1 = box_edit_address1.get()
    address_2 = box_edit_address2.get()
    city = box_edit_city.get()
    state = box_edit_state.get()
    zipcode = box_edit_zipcode.get()
    country = box_edit_country.get()
    phone = box_edit_phone.get()
    email = box_edit_email.get()
    payment_method = box_edit_payment_method.get()
    discount_code = box_edit_discount_code.get()
    price_paid = box_edit_price_paid.get()
    vals = (
        first_name,
        last_name,
        address_1,
        address_2,
        city,
        state,
        zipcode,
        country,
        phone,
        email,
        payment_method,
        discount_code,
        price_paid,
        id_to_edit
    )

    # Update record in database
    c.execute(sql_command, vals)
    conn.commit()

    # Close customer search/edit window
    tk_search_customers.destroy()


def write_to_csv(recs):
    # Get filepath to save to
    f_path = filedialog.asksaveasfilename(
        initialdir="C:/Users/garrisow/Desktop/practice/python/tkinter/data",
        title="Select A File",
        filetypes=(
            ("csv files", "*.csv"),
            ("all files", "*.*")
        )
    )

    # Suffix with .csv if required
    if not f_path.endswith("*.csv") and not f_path.endswith("*.CSV"):
        f_path = f_path + ".csv"

    # Write records to CSV
    with open(f_path, "w+", newline="") as f:
        for rec in recs:
            csv_writer = csv.writer(f, dialect="excel")
            csv_writer.writerow(rec)


# Main window
root = Tk()
root.title("CRM Tool")
root.iconbitmap("../images/favicon.ico")
root.geometry("400x800")

# Connect to database
conn = sqlite3.connect("../data/crm.db")
c = conn.cursor()

# Title label
lbl_title = Label(root, text="Customer Database", font=("Helvetica", 16))
lbl_title.grid(row=0, column=0, columnspan=2, pady=10)

# Labels for main form to enter customer data
lbl_first_name = Label(root, text="First Name")
lbl_last_name = Label(root, text="Last Name")
lbl_address1 = Label(root, text="Address 1")
lbl_address2 = Label(root, text="Address 2")
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
btn_list_customers = Button(
    root,
    text="List Customers",
    command=list_customers
)
btn_search_customers = Button(
    root,
    text="Search/Edit Customers",
    command=search_customers
)

# Add buttons to screen
btn_add_customer.grid(row=15, column=0, columnspan=2, padx=10, pady=10)
btn_clear_fields.grid(row=16, column=0, columnspan=2, padx=10, pady=10)
btn_list_customers.grid(row=17, column=0, columnspan=2, padx=10, pady=10)
btn_search_customers.grid(row=18, column=0, columnspan=2, padx=10, pady=10)

# Main loop
root.mainloop()

# Close database connection
conn.close()
