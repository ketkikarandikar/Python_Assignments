# Write a Python function that takes a list and returns a new list with unique
# elements of the first list.

def unique_elements(l1):   # initialization of unique elements
    unique_l1 = []   # empty list taken

    for s in l1:      
        if s not in unique_l1:    # if s is not in list then print the element
            unique_l1.append(s)

    for s in unique_l1:
        print(s)

l1 = [10,20,20,30,40,10]   # list of elements
print("The unique elements of the l1 are : ")   # print the unique elements
unique_elements(l1)  # calling the new list with unique elements

