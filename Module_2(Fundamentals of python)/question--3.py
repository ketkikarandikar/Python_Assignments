# Write a python program for fibonacci series ?


n = int(input("Enter number : "))   # input number


def Fibonacci(n):

 
    if n < 0:                 # If n is less than zero then will return incorrect number
        print("Incorrect number")
 
    elif n == 0:             # If n is 0 then will return 0
        return 0
 
    elif n == 1 or n == 2:        # If n is 1 or 2 it will return 1
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)    # Formula for fibonacci is => F(n) = F(n − 1) + F(n − 2)
    
print(Fibonacci(n))