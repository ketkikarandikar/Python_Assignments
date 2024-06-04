from file_handler import load_inventory, save_inventory, load_transactions, save_transactions

class Customer:
    def __init__(self):
        self.inventory = load_inventory()
        self.transactions = load_transactions()

    def buy_fruit(self, fruit_manager):
        """Buy fruit from the fruit manager."""
        name = input("Enter the name of the fruit you want to buy: ").strip().capitalize()
        quantity = int(input("Enter the quantity you want to buy: "))
        fruit_manager.sell_fruit(name, quantity)
        save_inventory(fruit_manager.inventory)
        save_transactions(fruit_manager.transactions)
