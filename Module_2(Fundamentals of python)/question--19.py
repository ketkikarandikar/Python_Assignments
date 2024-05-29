# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string.


k = input("Enter string : ")  # Enter the string from user

if 'not' in k and 'poor' in k:   # To replace the not and poor with good if the condition is true
    
    k = k.replace(k[k.find('not'):k.find('poor')+4], 'good') # to find and replace

print("New Str : ", k)  # to print the New string
