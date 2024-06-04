# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

import math   # import the math module

class Circle:  # take a class for circle
    def __init__(self, radius):  
        self.radius = radius

    def calculate_area(self):  # calculate the area
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):  # calculate the perimeter
        return 2 * math.pi * self.radius

# Create a circle with radius 5
circle = Circle(5)  # area of circle
# Calculate the area and perimeter of the circle
area = circle.calculate_area()   # formular to calculate area of circle
perimeter = circle.calculate_perimeter()  # formula to calculate the perimeter of the circle
print("Area of the circle:", area)  # print the area of the circle
print("Perimeter of the circle:", perimeter)  # print the perimeter of the circle
