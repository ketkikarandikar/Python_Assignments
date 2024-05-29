# Write a Python program to find the second smallest number in a list.

def find_len(l1):  # initializing to find the length of the list
	length = len(l1)  # to get the length of the list
	l1.sort()  # to sort the list
	print("Second Smallest element :", l1[1]) # to print the second smallest element in the list

l1=[2,4,6,8,10,1,3,5,7,9]  # List
find_len(l1)  # call the find_len 
