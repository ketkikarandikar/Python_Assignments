# Write a Python function to reverse a string if its length is a multiple of 4.


def sreverse():   # Define reverse
    str = input("Enter string : ")   # Enter the string or initialize.
    if len(str)%4==0:
        print("Reverse string is : ", str[::-1])     # -1 to reverse the string using the negative indexing
    else:
        print(str)

sreverse()
