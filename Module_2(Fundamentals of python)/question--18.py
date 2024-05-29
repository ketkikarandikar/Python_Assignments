# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.

s = input("Enter str : ")   # Enter String

if len(s) > 2:
    if s.endswith('ing'):       # using endswith we can check whether the string is ending with ing or ly
        s += 'ly'             # if ending with ing will add ly
    else:
        s += 'ing'             # if ending with ly other will add ing in the end
print(s)
