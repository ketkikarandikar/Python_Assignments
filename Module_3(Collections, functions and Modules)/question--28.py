# Write a Python program to remove an empty tuple(s) from a list of tuples.

k = [(10, 20, 30),(),(40, 50, 60),(),(70, 80, 90)]    # take a tuple

remove = []   # remove an empty tuple

for t in k:
    if t:
        remove.append(t)
# print the list after removing the empty tuple from the list
print(remove)