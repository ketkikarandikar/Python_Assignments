# Write a Python program to count the frequency of words in a file.

def count_word_frequency(file_path):
    word_frequency = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    word = word.strip(",.?!")  # Remove punctuation marks
                    word_frequency[word] = word_frequency.get(word, 0) + 1
    except FileNotFoundError:
        print("File not found!")
    return word_frequency

# Example usage:
file_path = "sample.txt"  # Replace "example.txt" with the path to your text file
word_frequency = count_word_frequency(file_path)
print("Word frequencies:", word_frequency)
