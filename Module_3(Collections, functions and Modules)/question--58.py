# Write a Python program to calculate the area of a parallelogram


def parallelogram_area(base, height):   # define the parallelogram area
    return base * height   # formula to calculate the parallelogram

# input base and height 
base = float(input("Enter the length of the base: "))
height = float(input("Enter the height: "))

# Calculate the area of the parallelogram
area = parallelogram_area(base, height)
print("Area of the parallelogram:", area)