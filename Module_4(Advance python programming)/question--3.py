# Write a Python program to read first n lines of a file. 

def read_first_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            for i in range(n):
                line = file.readline().rstrip('\n')  # Read each line and remove the newline character
                if line:
                    print(line)
                else:
                    break
    except FileNotFoundError:
        print("File not found!")

# Example usage:
file_path = "sample.txt"  # Replace "example.txt" with the path to your text file
n = 5  # Number of lines to read
read_first_n_lines(file_path, n)
