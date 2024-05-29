# Write a Python program to check multiple keys exists in a dictionary


# Initialize the dictionary
dict = {1: "Ketki", 2: "Karandikar", 3: "Neel", 4: "Golwelkar"}

# Key to check

check = [2,4,8]

# Check if the key exists in the dictionary

for key in check:
    if key in dict:
        print("The key '{key}' exists in the dictionary.")
    else:
        print("The key '{key}' does not exist in the dictionary.")

