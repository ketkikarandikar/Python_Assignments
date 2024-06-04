# Write a Python program to read an entire text file. 

def read_file(file_path): # Initialize the file to read
    try:
        with open(file_path, 'r') as file: # open the file
            content = file.read()  # read the content
            print(content) # print the content
    except FileNotFoundError:  
        print("File not found!")  # print the error

file_path = "sample.txt" # file path
read_file(file_path)  # read the file 
