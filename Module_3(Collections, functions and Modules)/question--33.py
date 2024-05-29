# Write a Python script to concatenate following dictionaries to create a new one.

t1_dict = {'kkr' : 'a', 'is' : 'b', 'rr' : 'c'}  # initializing dictionaries
t2_dict = {'rrk' : 'd', 'si' : 'e', 'rl' : 'f'}

# create a new dictionary by coping t1_dict
new_dict = t1_dict.copy()

# Update the new dictionary with the contents of t2_dict
new_dict.update(t2_dict)

# Print the new concatenated dictionary
print("Concatenated Dictionary:", new_dict)