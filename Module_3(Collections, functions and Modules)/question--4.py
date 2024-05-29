# Write a Python function to get the largest number, smallest num and sum of all from a list.


l = []

for i in range(1,6):     # To get any 5 input from user
    E = int(input("Enter number: "))     
    l.append(E)     #  To get the elements from E

print("Greatest number is : ", max(l))   # To find the largest number
print("Smallest number is : ", min(l))  # To find the smallest number

def add():    # initialization for the sum of all numbers
    print(sum(l))    

add()    # To call the add function
