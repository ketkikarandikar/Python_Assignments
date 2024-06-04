# Write python program that user to enter only odd numbers, else will raise an exception. 

class EvenNumberError(Exception):  # make a class for even number error
    """Custom exception class for handling even number input."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Error: {self.value} is an even number. Please enter only odd numbers."


def get_odd_number_from_user(): # definition for odd number
    while True:
        try:
            number = int(input("Enter an odd number: "))  # enter odd number
            if number % 2 == 0:  # for even number
                raise EvenNumberError(number)
            else:
                return number
        except ValueError:
            print("Error: Please enter a valid integer.")

try:
    odd_number = get_odd_number_from_user()
    print("You entered:", odd_number)
except EvenNumberError as e:
    print(e)
