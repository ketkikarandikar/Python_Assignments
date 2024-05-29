# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string: 'w3resource'
# Expected output:
# {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

Sample_string = 'w3resource'

# Initialize an empty dictionary to store counts of letters
letter = {}

# Iterate through each character in the string
for i in Sample_string:
    # Increase the count of the character in the dictionary
    letter[i] = letter.get(i, 0) + 1

# Print the result of the dictionary
print("Dictionary created from the string with letter counts:")
print(letter)