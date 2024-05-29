# Write a Python program to check a list is empty or not.

# defination to check the list is empty or not.
def fun(list):
    list = [10, 15, 20, 25, 30]  
    if len(list) == 0:   # To find if the list is empty or not.
        print("The list is empty")
    else:
        print(list)

list = []
if fun(list):
    print("The list is not empty.")  # If the list is empty
else:
    print("The list is empty.")

    

