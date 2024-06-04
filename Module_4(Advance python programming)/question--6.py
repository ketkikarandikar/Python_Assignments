# Write a Python program to read a file line by line store it into a variable. 

def read_file_into_variable(file_path):
    content = ""
    try:
        with open(file_path, 'r') as file:
            for line in file:
                content += line
    except FileNotFoundError:
        print("File not found!")
    return content

# Example usage:
file_path = "sample.txt"  # Replace "example.txt" with the path to your text file
file_content = read_file_into_variable(file_path)
print(file_content)
