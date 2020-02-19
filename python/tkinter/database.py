from tkinter import *
from PIL import ImageTk, Image  # Non-standard library `Pillow`
import sqlite3


def submit():
    # Connect to database, create cursor
    conn = sqlite3.connect("data/address_book.db")
    c = conn.cursor()

    # Insert into table
    c.execute(
        (
            "INSERT INTO addresses VALUES "
            + "(:first_name, :last_name, :address, :city, :state, :zipcode)"
        ),
        {
            "first_name": first_name.get(),
            "last_name": last_name.get(),
            "address": address.get(),
            "city": city.get(),
            "state": state.get(),
            "zipcode": zipcode.get()
        }
    )

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Clear the text boxes
    clear_textboxes()


def clear_textboxes():
    first_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def query():
    # Connect to database, create cursor
    conn = sqlite3.connect("data/address_book.db")
    c = conn.cursor()

    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()

    # Loop through results, adding to text for Label
    records_list = []
    for record in records:
        records_list.append(
            (
                str(record[6])
                + ": "
                + record[0]
                + " "
                + record[1]
                + "\n"
            )
        )
    print_records = "".join(records_list)
    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # Commit changes and close connection
    conn.commit()
    conn.close()


def delete():
    # Connect to database, create cursor
    conn = sqlite3.connect("data/address_book.db")
    c = conn.cursor()

    # Delete record
    delete_id = str(select_box.get())
    c.execute("DELETE FROM addresses WHERE oid = " + delete_id)

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Clear the Delete ID textbox
    select_box.delete(0, END)


def update():
    global update_window

    # Create second window for update
    update_window = Tk()
    update_window.title("Update A Record")
    update_window.iconbitmap("images/favicon.ico")

    # Globals for text boxes
    global update_first_name
    global update_last_name
    global update_address
    global update_city
    global update_state
    global update_zipcode

    # Create text box Entry widgets
    update_first_name = Entry(update_window, width=30)
    update_first_name.grid(row=0, column=1, padx=20, pady=(10, 0))
    update_last_name = Entry(update_window, width=30)
    update_last_name.grid(row=1, column=1)
    update_address = Entry(update_window, width=30)
    update_address.grid(row=2, column=1)
    update_city = Entry(update_window, width=30)
    update_city.grid(row=3, column=1)
    update_state = Entry(update_window, width=30)
    update_state.grid(row=4, column=1)
    update_zipcode = Entry(update_window, width=30)
    update_zipcode.grid(row=5, column=1)

    # Create text box Labels
    update_first_name_label = Label(update_window, text="First Name")
    update_first_name_label.grid(row=0, column=0, pady=(10, 0))
    update_last_name_label = Label(update_window, text="Last Name")
    update_last_name_label.grid(row=1, column=0)
    update_address_label = Label(update_window, text="Address")
    update_address_label.grid(row=2, column=0)
    update_city_label = Label(update_window, text="City")
    update_city_label.grid(row=3, column=0)
    update_state_label = Label(update_window, text="State")
    update_state_label.grid(row=4, column=0)
    update_zipcode_label = Label(update_window, text="Zip Code")
    update_zipcode_label.grid(row=5, column=0)

    # Create button to save updates
    save_button = Button(update_window, text="Save", command=save_update)
    save_button.grid(
        row=6,
        column=0,
        columnspan=2,
        pady=10, 
        padx=10, 
        ipadx=145
    )

    # Connect to database, create cursor
    conn = sqlite3.connect("data/address_book.db")
    c = conn.cursor()

    # Get selected record id
    update_id = str(select_box.get())

    # Query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + update_id)
    records = c.fetchall()

    # Loop through results and fill in Entry boxes
    for record in records:
        update_first_name.insert(0, record[0])
        update_last_name.insert(0, record[1])
        update_address.insert(0, record[2])
        update_city.insert(0, record[3])
        update_state.insert(0, record[4])
        update_zipcode.insert(0, record[5])

    # Commit changes and close connection
    conn.commit()
    conn.close()


def save_update():
    # Connect to database, create cursor
    conn = sqlite3.connect("data/address_book.db")
    c = conn.cursor()

    # Update record
    record_id = str(select_box.get())
    c.execute(
        (
            "UPDATE addresses SET "
            + "first_name = :first_name, "
            + "last_name = :last_name, "
            + "address = :address, "
            + "city = :city, "
            + "state = :state, "
            + "zipcode = :zipcode "
            + "WHERE oid =  :oid"
        ),
        {
            "first_name": update_first_name.get(),
            "last_name": update_last_name.get(),
            "address": update_address.get(),
            "city": update_city.get(),
            "state": update_state.get(),
            "zipcode": update_zipcode.get(),
            "oid": record_id
        }
    )

    # Commit changes and close connection
    conn.commit()
    conn.close()

    # Clear the Delete ID textbox
    select_box.delete(0, END)

    #
    update_window.destroy()


# Create root with title and favicon
root = Tk()
root.title("Database Exercise")
root.iconbitmap("images/favicon.ico")
root.geometry("400x600")

# Create a database or connect to one
conn = sqlite3.connect("data/address_book.db")

# Create cursor
c = conn.cursor()

# Create table - commenting out since this only had to be done once
# c.execute(
#     "CREATE TABLE addresses ("
#     + "first_name text, "
#     + "last_name text, "
#     + "address text, "
#     + "city text, "
#     + "state text, "
#     + "zipcode integer"
#     + ")"
# )

# Create text box Entry widgets
first_name = Entry(root, width=30)
first_name.grid(row=0, column=1, padx=20, pady=(10, 0))
last_name = Entry(root, width=30)
last_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

# Create text box Labels
first_name_label = Label(root, text="First Name")
first_name_label.grid(row=0, column=0, pady=(10, 0))
last_name_label = Label(root, text="Last Name")
last_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zip Code")
zipcode_label.grid(row=5, column=0)

# Create submit Button
submit_button = Button(root, text="Add Record To Database", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create query Button
query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=128)

# Create select box and Label
select_box = Entry(root, width=30)
select_box.grid(row=9, column=1, pady=(20, 0))
select_box_label = Label(root, text="Select ID")
select_box_label.grid(row=9, column=0, pady=(20, 0))

# Delete and update buttons
delete_button = Button(root, text="Delete Record", command=delete)
delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=128)
update_button = Button(root, text="Update Record", command=update)
update_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=128)

# Commit changes
conn.commit()

# Close connection
conn.close()

# Main loop
root.mainloop()