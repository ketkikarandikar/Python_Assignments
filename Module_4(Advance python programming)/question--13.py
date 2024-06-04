# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

# Example usage:
# Create a rectangle with length 5 and width 3
rectangle = Rectangle(5, 3)
# Compute the area of the rectangle
area = rectangle.compute_area()
print("Area of the rectangle:", area)
