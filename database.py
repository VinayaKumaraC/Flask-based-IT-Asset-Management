import sqlite3
from werkzeug.security import generate_password_hash

# DATABASE CONNECTION

conn = sqlite3.connect("assets.db")
cursor = conn.cursor()

# =========================
# USERS TABLE
# =========================

cursor.execute("""

CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT UNIQUE NOT NULL,

    password TEXT NOT NULL,

    role TEXT NOT NULL DEFAULT 'user'

)

""")

# =========================
# ASSETS TABLE
# =========================

cursor.execute("""

CREATE TABLE IF NOT EXISTS assets (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    asset_name TEXT NOT NULL,

    asset_type TEXT NOT NULL,

    serial_number TEXT UNIQUE NOT NULL,

    status TEXT NOT NULL

)

""")

# =========================
# EMPLOYEES TABLE
# =========================

cursor.execute("""

CREATE TABLE IF NOT EXISTS employees (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    employee_name TEXT NOT NULL,

    department TEXT NOT NULL

)

""")

# =========================
# ASSIGNMENTS TABLE
# =========================

cursor.execute("""

CREATE TABLE IF NOT EXISTS assignments (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    asset_id INTEGER NOT NULL,

    employee_id INTEGER NOT NULL,

    assigned_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (asset_id) REFERENCES assets(id),

    FOREIGN KEY (employee_id) REFERENCES employees(id)

)

""")

# =========================
# DEFAULT ADMIN ACCOUNT
# =========================

admin_password = generate_password_hash("admin123")

cursor.execute("""

INSERT OR IGNORE INTO users (

    id,
    username,
    password,
    role

)

VALUES (?, ?, ?, ?)

""", (

    1,
    "admin",
    admin_password,
    "admin"

))

# =========================
# DEFAULT USER ACCOUNT
# =========================

user_password = generate_password_hash("user123")

cursor.execute("""

INSERT OR IGNORE INTO users (

    id,
    username,
    password,
    role

)

VALUES (?, ?, ?, ?)

""", (

    2,
    "user",
    user_password,
    "user"

))

# =========================
# SAVE DATABASE
# =========================

conn.commit()
conn.close()

# =========================
# SUCCESS MESSAGE
# =========================

print("===================================")
print(" Database Created Successfully ")
print("===================================")

print("Admin Login")
print("------------------------------")
print("Username : admin")
print("Password : admin123")
print("------------------------------")

print("User Login")
print("------------------------------")
print("Username : user")
print("Password : user123")
print("------------------------------")
