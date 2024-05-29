# Write a Python program to generate and print a list of first and last 5
# elements where the values are square of numbers between 1 and 30.


def Values_1():

    l = list()
    for i in range(1, 31):
        l.append(i*i)
    print(l[:5])          # Print the first 5 elements of the list 'l'
    print(l[-5:])         # Print the last 5 elements of the list 'l'
    print(l)
Values_1()   # call the values_1