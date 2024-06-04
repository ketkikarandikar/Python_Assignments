

from fruit_manager import FruitManager
from customer import Customer

def display_menu():
    """Display the Fruit Store Menu."""
    print("\nFruit Store Menu:")
    print("1. Display Inventory")
    print("2. Buy Fruit")
    print("3. Add Fruit Stock")
    print("4. Update Fruit Stock")
    print("5. Exit")

def get_valid_option(options):
    """Get a valid menu option from the user."""
    while True:
        choice = input("Please enter your choice: ").strip()
        if choice.isdigit() and int(choice) in options:
            return int(choice)
        else:
            print("Invalid choice. Please enter a valid option.")

def main():
    fruit_manager = FruitManager()
    customer = Customer()

    while True:
        display_menu()
        choice = get_valid_option([1, 2, 3, 4, 5])

        try:
            if choice == 1:
                fruit_manager.display_inventory()
            elif choice == 2:
                customer.buy_fruit(fruit_manager)
            elif choice == 3:
                fruit_manager.add_fruit_stock()
            elif choice == 4:
                fruit_manager.update_fruit_stock()
            elif choice == 5:
                print("Thank you for visiting the Fruit Store!")
                break
            print("Menu displayed again.")
        except Exception as e:
            print(f"An error occurred: {e}. Returning to the previous menu.")

if __name__ == "__main__":
    main()
