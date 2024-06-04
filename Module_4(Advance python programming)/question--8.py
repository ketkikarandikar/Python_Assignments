# Write a Python program to count the number of lines in a text file.

def count_lines(file_path):
    line_count = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line_count += 1
    except FileNotFoundError:
        print("File not found!")
    return line_count

# Example usage:
file_path = "sample.txt"  # Replace "example.txt" with the path to your text file
number_of_lines = count_lines(file_path)
print("Number of lines in the file:", number_of_lines)
