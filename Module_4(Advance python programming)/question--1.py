# Write a Python program to read an entire text file. 

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found!")

file_path = "sample.txt" 
read_file(file_path)
