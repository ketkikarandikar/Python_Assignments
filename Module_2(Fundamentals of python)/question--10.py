# Write a Python program that will return true if the two given integer values are equal or their sum 
# or difference is 5 ?
x = int(input("Enter num1 : "))
y = int(input("Enter num2 : "))   # Boolean type
                                               
if x==y or (x - y) == 5 or (x + y) == 5:     # will print true if the addition or substraction of the values
    print("True")                               # are equal to 5
else:                                           # or will print False
    print("False")
