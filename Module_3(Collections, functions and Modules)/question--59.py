# Write a Python program to calculate surface volume and area of a cylinder

import math   # Import math module

# Input radius and height
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculate surface area
surface_area = 2 * math.pi * radius * (radius + height)
# Calculate volume
volume = math.pi * radius**2 * height

print("Surface area of the cylinder:", surface_area)
print("Volume of the cylinder:", volume)