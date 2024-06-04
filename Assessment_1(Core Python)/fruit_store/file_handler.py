import json

def load_inventory():
    """Load inventory from file."""
    try:
        with open("inventory.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Inventory file not found. Starting with empty inventory.")
        return []

def save_inventory(inventory):
    """Save inventory to file."""
    with open("inventory.json", "w") as file:
        json.dump([fruit.__dict__ for fruit in inventory], file, indent=4)

def load_transactions():
    """Load transactions from file."""
    try:
        with open("transactions.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Transactions file not found. Starting with empty transactions.")
        return []

def save_transactions(transactions):
    """Save transactions to file."""
    with open("transactions.json", "w") as file:
        json.dump(transactions, file, indent=4)

def log_transaction(transaction):
    """Log a transaction to the log file."""
    with open("transaction_log.txt", "a") as file:
        file.write(json.dumps(transaction) + "\n")
