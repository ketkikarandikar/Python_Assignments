# Write a Python program to count the frequency of words in a file.

def count_word_frequency(file_path): # defination to count the word frequency
    word_frequency = {}  # take an empty set
    try:
        with open(file_path, 'r') as file:  # open a file
            for line in file:
                words = line.split()  # split line into words
                for word in words:
                    word = word.strip(",.?!")  # Remove punctuation marks
                    word_frequency[word] = word_frequency.get(word, 0) + 1
    except FileNotFoundError:
        print("File not found!")
    return word_frequency

file_path = "sample.txt"  
word_frequency = count_word_frequency(file_path)
print("Word frequencies:", word_frequency)   # print the frequency of the words means how many times the words are there in the sentence
