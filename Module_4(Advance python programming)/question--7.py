# Write a python program to find the longest words.

def find_longest_words(file_path): # defination to find the longest word
    longest_words = []  # take an empty list
    max_length = 0  # max length

    try:
        with open(file_path, 'r') as file: # open a file
            for line in file:
                words = line.split()  # Split the line into words
                for word in words:
                    word = word.strip(",.?!")  # Remove punctuation marks
                    if len(word) > max_length: # get the length
                        longest_words = [word]  
                        max_length = len(word)  # store the max length
                    elif len(word) == max_length:
                        longest_words.append(word)
    except FileNotFoundError:
        print("File not found!")  # except an error

    return longest_words

file_path = "sample.txt" 
longest_words = find_longest_words(file_path)
print("Longest words:", longest_words) # print the longest word from the sentence
