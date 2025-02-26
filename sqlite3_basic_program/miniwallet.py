import sqlite3


# Connect to database (creates the file if it doesn't exist)
# conn = sqlite3.connect("programs/database.db")


def check_balance(name):
    conn = sqlite3.connect("programs/database.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT balance FROM users WHERE name = ?", (name,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result:
        return f"{name}'s balance: ${result[0]:.2f}"
    else:
        return "User not found!"

def add_money(name, amount):
    conn = sqlite3.connect("programs/database.db")
    cursor = conn.cursor()
    
    cursor.execute("UPDATE users SET balance = balance + ? WHERE name = ?", (amount, name))
    conn.commit()
    conn.close()
    
    return f"${amount} added to {name}'s wallet!"

# Example usage
print(check_balance("Alice"))  # Check Alice's balance
print(add_money("Alice", 200))  # Add $200 to Alice's wallet
print(check_balance("Alice"))  # Check again

