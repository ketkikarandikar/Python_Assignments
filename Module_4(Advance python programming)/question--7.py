# Write a python program to find the longest words.

def find_longest_words(file_path):
    longest_words = []
    max_length = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()  # Split the line into words
                for word in words:
                    word = word.strip(",.?!")  # Remove punctuation marks
                    if len(word) > max_length:
                        longest_words = [word]
                        max_length = len(word)
                    elif len(word) == max_length:
                        longest_words.append(word)
    except FileNotFoundError:
        print("File not found!")

    return longest_words

# Example usage:
file_path = "sample.txt"  # Replace "example.txt" with the path to your text file
longest_words = find_longest_words(file_path)
print("Longest words:", longest_words)
