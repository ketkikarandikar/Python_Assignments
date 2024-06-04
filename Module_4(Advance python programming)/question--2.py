# Write a Python program to append text to a file and display the text.

def append_to_file(file_path, text_to_append):
    try:
        with open(file_path, 'a') as file:
            file.write(text_to_append)
    except FileNotFoundError:
        print("File not found!")

def display_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found!")

# Example usage:
file_path = "sample.txt"  # Replace "example.txt" with the path to your text file
text_to_append = "\nThis is some additional text to append."
append_to_file(file_path, text_to_append)
print("Updated contents:")
display_file_contents(file_path)
