# Write a python program to check if a number is positive, negative or zero ?

"""
n=int(input("Enter number : "))
x=["positive" if n>0 else "negative" if n<0 else "zero" ]    # For Eqaual to zero number will print Eqaual to zero
print(x)                                                     # For positive number will print positive
                                                             # For negative number will print negative
"""                                               

# Used If elif and else loop 

n=int(input("Enter number : "))    # Input number or initialize

if n>0:
    print("Positive")     # For positive number will print positive

elif n<0:
    print("Negative")    # For negative number will print negative

else:
    print("Neither negative nor positive.")  # For Eqaual to zero number will print Eqaual to zero
