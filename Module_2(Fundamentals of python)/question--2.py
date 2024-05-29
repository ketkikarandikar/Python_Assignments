# Write a python program to get the Factorial number of given number ?

n = int (input ("Enter a number: "))   # input number
factorial = 1                          # As factorial of zero and 1 is always 1
if n >= 1:
    for i in range (1, n+1):             # started from 1 
        factorial=factorial *i         # multiply the numbers till the given number by user
print("Factorial of the given number is: ", factorial)
