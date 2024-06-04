# Write a Python program to read last n lines of a file. 

def read_last_n_lines(file_path, n): # defination read the last n lines of a file
    try:
        with open(file_path, 'r') as file:  # open a file
            lines = file.readlines()  # to read the lines
            last_n_lines = lines[-n:]  # to go to the end and read lines
            for line in last_n_lines:
                print(line.rstrip('\n'))  # to remove the new line character
    except FileNotFoundError:
        print("File not found!")  # except the error

file_path = "sample.txt"  
n = 5  # Number of lines to read from the end
read_last_n_lines(file_path, n)
