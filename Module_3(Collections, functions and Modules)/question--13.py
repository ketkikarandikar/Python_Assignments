# Write a Python program to select an item randomly from a list.

import random

t_item = ['Rose','Grape','Vine','Red','Sky','Earth']

print("Original item is : " + str(t_item))

random_item = random.choice(t_item)

print("Random selected item is : " + str(random_item))


