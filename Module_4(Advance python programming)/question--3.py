# Write a Python program to read first n lines of a file. 

def read_first_n_lines(file_path, n):  # defination to read first n lines of a file
    try:
        with open(file_path, 'r') as file:  # open a file
            for i in range(n):  # take range till n 
                line = file.readline().rstrip('\n')  # Read each line and remove the newline character
                if line:
                    print(line)
                else:
                    break
    except FileNotFoundError:
        print("File not found!")  # except an error 

file_path = "sample.txt" 
n = 5  # Number of lines to read
read_first_n_lines(file_path, n)
