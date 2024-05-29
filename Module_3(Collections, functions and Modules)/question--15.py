# Write a Python program to get unique values from a list

l1 = [1,2,3,4,5,5,6,10,14,2,1,1,1,1,2,2,3,4]  # Create a list

l2 = []  # take an empty list

for value in l1:
    if value not in l2:  # if value not in list add the value
        l2.append(value)   # append the values


print("Original list :", l1)   # print the original values
print("Unique list :", l2)     # print the unique values
