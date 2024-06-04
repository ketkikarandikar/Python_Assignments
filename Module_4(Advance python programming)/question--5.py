# Write a Python program to read a file line by line and store it into a list

def read_file_lines(file_path):
    lines = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                lines.append(line.strip())  # Strip removes leading and trailing whitespaces including '\n'
    except FileNotFoundError:
        print("File not found!")
    return lines

# Example usage:
file_path = "sample.txt"  # Replace "example.txt" with the path to your text file
lines_list = read_file_lines(file_path)
print(lines_list)
