# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.

n1 = input("Enter str1 : ")             # Input numbers
n2 = input("Enter str2 : ")             

print("Before swaping str of A :", n1)        
print("Before swaping str of B :", n2)   # will print the numbers before swaping

n1,n2 = n2,n1          # swap numbers without usinf temp

print("After swaping str of A :", n1)   # will swap the numbers and print
print("After swaping str of B :", n2)

# By using the temp variable

n1 = input("Enter str1 : ")
n2 = input("Enter str2 : ")

print("Before swaping str of A :", n1)     # will print the numbers before swaping
print("Before swaping str of B :", n2)     

temp = n1   # swap numbers using temp variable
n1 = n2
n2 = temp

print("After swaping str of A :", n1)   # will swap and print the numbers
print("After swaping str of B :", n2)

