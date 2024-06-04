class Fruit:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def sell(self, quantity_sold):
        if self.quantity >= quantity_sold:
            self.quantity -= quantity_sold
            return True
        else:
            return False


