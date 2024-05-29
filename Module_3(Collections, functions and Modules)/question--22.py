# Write a Python program to check whether an element exists within a tuple.

t = (10,9,8,7,6)

element = int(input("Enter element : "))

if element in t:
    print("The element {element} is present in the tuple.")

else:
    print("The element {element} is not present in the tuple.")