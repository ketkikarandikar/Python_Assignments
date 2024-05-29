# Write a Python program to map two lists into a dictionary

l1 = [1, 2, 3, 4, 5, 6]   # Initialize list1

l2 = ["T-shirt", "Skirt", "Jeans", "western wear", "Plazo", "Kurtis"]  # List 2

d = {}   # dictionary

for i in range(len(l1)):     
    # Use index to access items from l1 and l2
    key = l1[i]
    value = l2[i]
    d[key] = value

print(d)