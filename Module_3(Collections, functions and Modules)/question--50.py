# Write a Python function to check whether a number is perfect or not.

def perfect_number(number):    # Initialize sum
    sum_num = 0
    
    # Find all factors of the number
    for i in range(1, number):
        if number % i == 0:
            sum_num += i
    
    # Check if the sum of factors equals the number itself
    return sum_num == number

# Input number
num = int(input("Enter a number: "))

# to check the number is perfect or not and print the result
if perfect_number(num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")