# Write a Python program to read a file line by line store it into a variable. 

def read_file_into_variable(file_path): # defination to read file
    content = ""  # empty string to store as a variable
    try:
        with open(file_path, 'r') as file:  # open a file
            for line in file:
                content += line  # add a line
    except FileNotFoundError:
        print("File not found!")
    return content

file_path = "sample.txt"  
file_content = read_file_into_variable(file_path)
print(file_content)  # to print the file content
