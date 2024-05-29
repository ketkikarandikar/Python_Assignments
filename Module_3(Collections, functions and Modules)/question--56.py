# Write a Python program to convert degree to radian

import math    # import math module

def degrees_to_radians(degrees):   # Define degree to radian 
    return degrees * (math.pi / 180)     # formula to convert degree to radian

# input the degree
degrees = float(input("Enter degrees: "))

# Convert degree to radian
radians = degrees_to_radians(degrees)
print(f"{degrees} degrees is equal to {radians} radians")