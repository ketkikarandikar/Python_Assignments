# Write a Python program to check whether a list contains a sub list


l1 = [10,9,8,7,6,5,4,3,2,1]  # list 1 initialization

# second list or sublist initialization 
l2 = [8,7,6,5]

# to check if secondlist is found in the first list
if l2 in [l1[i:i+len(l2)] for i in range(len(l1) - len(l2) + 1)]:
    print("Sub list is in the first list.")
else:
    print("Sub list is not in the first list.")
