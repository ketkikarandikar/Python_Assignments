# Write a Python program to replace last value of tuples in a list.

k = [(10, 20, 30),(40, 50, 60),(70, 80, 90)]  # to replace the last value

print([t[:-1] + (100,) for t in k]) # take negative indexing add 100 at the end
