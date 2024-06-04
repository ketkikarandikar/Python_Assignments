# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

def find_max_min(decimal_numbers):
    maximum = max(decimal_numbers)
    minimum = min(decimal_numbers)
    return maximum, minimum

decimal_numbers = [3.14, 2.71, 1.618, 4.669, 0.577]
maximum, minimum = find_max_min(decimal_numbers)
print("Maximum number:", maximum)
print("Minimum number:", minimum)
