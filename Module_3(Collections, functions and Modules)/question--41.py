# Write a Python program to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

d1 = {"a": 100, "b": 200, "c":300}

d2 = {"a": 300, "b": 200, "d" :400}

dict = {}

# Add values from d1
for i, j in d1.items():
    dict[i] = j

# Add values from d2
for i, j in d2.items():
    if i in dict:
        dict[i] += j
    else:
        dict[i] = j

print("Combined Dictionary:", dict)