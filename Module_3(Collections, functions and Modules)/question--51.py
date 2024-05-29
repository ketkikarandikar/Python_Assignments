# Write a Python function that checks whether a passed string is palindrome or not

def is_palindrome(s):    # Initialize
    return s == s[::-1]   

# Input String
string = input("Enter a string: ")

# Check if String is palindrome or not
if is_palindrome(string):
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
    