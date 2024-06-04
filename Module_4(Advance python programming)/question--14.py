# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle 

import math  # import math module

class Circle:  # make a class for circle
    def __init__(self, radius):  
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

# Create a circle with radius 5
circle = Circle(5)
# Calculate the area and perimeter of the circle
area = circle.calculate_area()  # calculate the area of circle
perimeter = circle.calculate_perimeter()  # calculate the perimeter of circle
print("Area of the circle:", area)  # print the area of the circle
print("Perimeter of the circle:", perimeter)  # Print the perimeter of the circle
