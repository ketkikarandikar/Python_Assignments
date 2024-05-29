# Write python program that swap two number with temp variable and without temp variable ?

# without using the temp variable

n1 = int(input("Enter Number1 : "))              # Input numbers
n2 = int(input("Enter Number2 : "))             

print("Before swaping value of A :", n1)        
print("Before swaping value of B :", n2)   # will print the numbers before swaping

n1,n2 = n2,n1          # swap numbers without usinf temp

print("After swaping value of A :", n1)   # will swap the numbers and print
print("After swaping value of B :", n2)

# By using the temp variable

n1 = int(input("Enter Number1 : "))
n2 = int(input("Enter Number2 : "))

print("Before swaping value of A :", n1)     # will print the numbers before swaping
print("Before swaping value of B :", n2)     

temp = n1   # swap numbers using temp variable
n1 = n2
n2 = temp

print("After swaping value of A :", n1)   # will swap and print the numbers
print("After swaping value of B :", n2)


