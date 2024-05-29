# Write a Python function to calculate the factorial of a number (a nonnegative integer)

def factorial():
    num = int(input("Enter Factorial number: "))   # inupt number
    
    # Check if zero
    if num == 0:
        return print("Number is zero")  # If the number is zero, print a message and exit the function
    
    else:
        # Initialize the factorial variable to 1
        fact = 1
        
        # Calculate the factorial using a loop
        for i in range(1, num + 1):
            fact = fact * i  # Multiply the current value of factorial by the current value of i
        
        print("Factorial of", num, "is", fact)

factorial()  # Call factorial