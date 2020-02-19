import sqlite3

# Create database and cursor
conn = sqlite3.connect("../data/crm.db")
c = conn.cursor()

# Create table
c.execute(
    "CREATE TABLE customers ("
    + "first_name TEXT, "
    + "last_name TEXT, "
    + "zipcode INTEGER, "
    + "price_paid REAL, "
    + "user_id INTEGER PRIMARY KEY AUTOINCREMENT"
    + ")"
)
