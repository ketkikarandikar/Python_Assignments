# How will you remove last object from a list?
# Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?

# We can remove the last object from a list by using remove and pop method

# To remove the last elemnet of the list :

list1 = [2, 33, 222, 14, 25] 

print(list1[-1])  # To print the last element using negative indexing

list1.remove(25) # Using remove method
print(list1)

list1 = [2, 33, 222, 14, 25] 


list1.pop()  # To remove the last element from list using pop method

print(list1)

