# How Do You Traverse Through A Dictionary Object In Python?

# Using the keys() method in Python allows you to iterate through the keys of a dictionary,
# providing a straightforward way to access and manipulate the dictionary's structure. 
# This method returns a view object that displays a list of all the keys in the dictionary.

# Define a sample dictionary

fruit_prices = {'apple': 50, 'banana': 20, 'orange': 40, 'grape': 60}   

# Iterate through keys using keys()

for fruit in fruit_prices.keys():

    print(f"The price of {fruit} is {fruit_prices[fruit]} rupees.")   # print the fruit and its price