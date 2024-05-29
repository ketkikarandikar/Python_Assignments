# Write a Python program to print all unique values in a dictionary.

dict = {1: "Ketki", 2: "Karandikar", 3: "Neel", 4: "Golwelkar"}


# To store unique values
unique = set()

# Iterate over the values of the dictionary
for i in dict.values():
    unique.add(i)     # add the values to the set

print("Unique Values:", unique)   # print unique values