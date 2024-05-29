# Why Do You Use the Zip () Method in Python?

# The zip() function in Python is used to combine two or more iterable dictionaries into a single iterable, 
# where corresponding elements from the input iterable are paired together as tuples.

fruits = ['Apple', 'Banana', 'Grapes']    # keys
prices = [50, 20, 60]  # values

new_dict = {fruits: prices for fruits,
			prices in zip(fruits, prices)}     # new dictionary with values and keys
print(new_dict)    # print the new dictionary
