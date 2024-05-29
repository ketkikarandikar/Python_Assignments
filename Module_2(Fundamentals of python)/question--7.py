# Write a Python program to find whether a given number is even or odd, print out an 
#appropriate message to the user ?


n = int(input("Enter n : "))    # input number

# For Odd and Even numbers

if n==0:
    print(n, "is nither even nor odd")    # For neither even nor odd

elif n%2==0:
    print(n,"is even")       # For even numbers will print even 

else:
    print(n,"is odd")       # For odd numbers will print odd
