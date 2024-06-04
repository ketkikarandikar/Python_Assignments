from models import Fruit
from file_handler import load_inventory, save_inventory, load_transactions, save_transactions

class FruitManager:
    def __init__(self):
        self.inventory = load_inventory()
        self.transactions = load_transactions()

    def add_fruit(self, name, price, quantity):
        """Add a new fruit to the inventory."""
        fruit = Fruit(name, price, quantity)
        self.inventory.append(fruit)
        self.transactions.append({"action": "add", "name": name, "quantity": quantity})
        save_inventory(self.inventory)
        save_transactions(self.transactions)

    def display_inventory(self):
        """Display the current inventory of fruits."""
        print("Fruit Inventory:")
        for fruit in self.inventory:
            print(f"{fruit.name}: ${fruit.price} per unit - Quantity: {fruit.quantity}")

    def add_fruit_stock(self):
        """Add fruit stock to the inventory."""
        try:
            name = input("Enter the name of the fruit: ").strip().capitalize()
            price = float(input("Enter the price of the fruit: "))
            quantity = int(input("Enter the quantity to add: "))
            self.add_fruit(name, price, quantity)
            print(f"{quantity} {name}(s) added to the inventory.")
        except Exception as e:
            print(f"An error occurred: {e}. Returning to the previous menu.")

    def update_fruit_stock(self):
        """Update the stock quantity of a fruit."""
        try:
            name = input("Enter the name of the fruit: ").strip().capitalize()
            new_quantity = int(input("Enter the new quantity: "))
            for fruit in self.inventory:
                if fruit.name.lower() == name.lower():
                    old_quantity = fruit.quantity
                    fruit.quantity = new_quantity
                    self.transactions.append({"action": "update", "name": name, "old_quantity": old_quantity, "new_quantity": new_quantity})
                    save_inventory(self.inventory)
                    save_transactions(self.transactions)
                    print(f"Stock for {name} updated successfully to {new_quantity}.")
                    return
            print("Sorry, we don't have that fruit in stock.")
        except Exception as e:
            print(f"An error occurred: {e}. Returning to the previous menu.")
