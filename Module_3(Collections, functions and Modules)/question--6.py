# Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given
# list of strings.

def check_words(str):
    count = 0
    for s in str:
        if len(s) > 1 and s[0] == s[-1]:
            count += 1

    return count

list = ['Ketki', 'After', 'Alpha', 'BetB', 'Gama', '220', '625', 'aba']

print("The number of strings where the first and last character are same from a given list of strings :  ", check_words(list))

