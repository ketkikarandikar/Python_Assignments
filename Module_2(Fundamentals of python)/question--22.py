# Write a Python program to get a string made of the first 2 and the last
# 2 chars from a given a string. If the string length is less than 2, return
# instead of the empty string.

def string_starts_ends(str):   # Define the string start and end
    
    str = input("Enter the string : ")    # Get the user defined string as input
    
    if len(str) < 2:    # If the length of string is less than 2
    
        return ''    # return the same string
    
    return str[0:2] + str[-2:]    # If more than 2 then print the first 2 characters of the string
                                   # and last 2 characters of the string

print(string_starts_ends(str))           
