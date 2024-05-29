# Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
# 300}, o {'item': 'item1', 'amount': 750}]
# Expected Output:
# Counter ({'item1': 1150, 'item2': 300})

Sample_data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

# combine values
combine = {}

for i in Sample_data:
    item = i['item']      # take item in dictionary
    amount = i['amount']   # take amount in dictionary
    if item in combine:
        combine[item] += amount
    else:
        combine[item] = amount

# Print the combined values
print("Combined values:")
print(combine)