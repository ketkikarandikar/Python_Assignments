from .models import Fruit


class FruitStoreController:
    def __init__(self):
        self.inventory = []

    def add_fruit(self, fruit):
        self.inventory.append(fruit)

    def display_inventory(self):
        print("Fruit Inventory:")
        for fruit in self.inventory:
            print(f"{fruit.name}: ${fruit.price} per unit - Quantity: {fruit.quantity}")

    def sell_fruit(self, fruit_name, quantity):
        for fruit in self.inventory:
            if fruit.name.lower() == fruit_name.lower():
                if fruit.sell(quantity):
                    print(f"{quantity} {fruit_name}(s) sold successfully!")
                else:
                    print(f"Sorry, we don't have enough quantity for {fruit_name}.")
                return
        print("Sorry, we don't have that fruit in stock.")
