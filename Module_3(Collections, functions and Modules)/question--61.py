# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

def find_max_min(decimal_numbers):  # defination to find the maximum and minimum numbers
    maximum = max(decimal_numbers)  # max numbers
    minimum = min(decimal_numbers)  # min numbers
    return maximum, minimum

decimal_numbers = [3.14, 2.71, 1.618, 4.669, 0.577]  # get a list
maximum, minimum = find_max_min(decimal_numbers)  # find the min and max
print("Maximum number:", maximum)  # print the max numbers
print("Minimum number:", minimum) # print the min numbers
