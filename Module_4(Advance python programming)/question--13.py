# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class Rectangle:  # build a class for rectangle
    def __init__(self, length, width):  # get the length and width
        self.length = length
        self.width = width

    def calculate_area(self):  # get the area of rectangle
        return self.length * self.width

# Create a rectangle with length 5 and width 3
rectangle = Rectangle(5, 3)
# Calculate the area of the rectangle
area = rectangle.calculate_area()   # formula of area of rectangle
print("Area of the rectangle:", area)  # print the area of rectangle
