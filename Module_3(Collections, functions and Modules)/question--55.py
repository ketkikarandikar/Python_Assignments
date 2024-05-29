# How will you randomizes the items of a list in place?

import random   # Import random

my_list = [10,20,30,40,50]   # List

shuffled_list = sorted(my_list, key=lambda x: random.random())   # Shuffle the list

print("Original list:", my_list)   # Print the original list
print("Shuffled list:", shuffled_list)   # Print the shuffeled list
