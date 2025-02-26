import sqlite3

# Connect and creates the file if it doesn't exist
conn = sqlite3.connect("programs/database.db")

cursor = conn.cursor()


# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     balance REAL NOT NULL
# )
# """)


# Insert data
# cursor.execute("INSERT INTO users (name, balance) VALUES (?, ?)", ("Alice", 1000))
# cursor.execute("INSERT INTO users (name, balance) VALUES (?, ?)", ("Bob", 500))

#delete Data
# cursor.execute("DELETE FROM users WHERE name = ?", ("Alice",))

#display all data
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
for user in users:
    print(user)

# Update data
# cursor.execute("UPDATE users SET balance = ? WHERE name = ?", (1200, "Alice"))

conn.commit()
conn.close()

