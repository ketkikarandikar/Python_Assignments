# Write a Python program to calculate the area of a trapezoid


def trapezoid_area(base1, base2, height):   # Define the trapezoid
    return (base1 + base2) * height / 2   # formula for to calculate trapezoid

# Input numbers
base1 = float(input("Enter the length of the first base: "))
base2 = float(input("Enter the length of the second base: "))
height = float(input("Enter the height: "))

# print the area of trapezoid
area = trapezoid_area(base1, base2, height)
print("Area of the trapezoid:", area)