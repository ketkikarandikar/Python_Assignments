# Write a Python program to read last n lines of a file. 

def read_last_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            last_n_lines = lines[-n:]
            for line in last_n_lines:
                print(line.rstrip('\n'))
    except FileNotFoundError:
        print("File not found!")

# Example usage:
file_path = "sample.txt"  # Replace "example.txt" with the path to your text file
n = 5  # Number of lines to read from the end
read_last_n_lines(file_path, n)
