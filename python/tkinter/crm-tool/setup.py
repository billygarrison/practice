import sqlite3

# Create database and cursor
conn = sqlite3.connect("../data/crm.db")
c = conn.cursor()

# Create table
c.execute(
    "CREATE TABLE IF NOT EXISTS customers ("
    + "first_name TEXT, "
    + "last_name TEXT, "
    + "zipcode INTEGER, "
    + "price_paid REAL, "
    + "user_id INTEGER PRIMARY KEY AUTOINCREMENT"
    + ")"
)

# Add more fields
new_fields = [
    "email TEXT",
    "address_1 TEXT",
    "address_2 TEXT",
    "city TEXT",
    "state TEXT",
    "country TEXT",
    "phone TEXT",
    "payment_method TEXT",
    "discount_code TEXT",
]
for field in new_fields:
    c.execute("ALTER TABLE customers ADD COLUMN " + field)
