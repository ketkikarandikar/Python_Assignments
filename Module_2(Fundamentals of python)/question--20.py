# Write a Python function that takes a list of words and returns the length of the longest one.

def find_longest_word(words_list):   # Define the longest word
    word_len = []   # Blank list 

    for n in words_list:   # for n number of words in a given list
        
        word_len.append((len(n), n))    # append to add words in a list

    word_len.sort()   # sort for sorting the list of words

    return word_len[-1][0], word_len[-1][1]    # to return the length of the words given in a list

result = find_longest_word(["Macroni", "Red Souce Pasta", "IceCream"])   # give the input

print("\nLongest word: ", result[1])   # To print the longest word
print("Length of the longest word: ", result[0])  # To print the Length of the longest word
