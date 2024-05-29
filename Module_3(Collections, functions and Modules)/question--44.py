# Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.
# Sample data: {'1': ['a','b'], '2': ['c','d']}
# Expected Output:
# ac ad bc bd

Sample_data = {'1': ['a','b'], '2': ['c','d']}

# Iterate through the values of the first key
for i in Sample_data['1']:
    # Iterate through the values of the second key
    for j in Sample_data['2']:
        # Print the combination of letters on separate lines
        print(i + j)