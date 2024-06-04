# Write a Python program to append text to a file and display the text.

def append_to_file(file_path, text_to_append): # defination to append a sentence in a file
    try:
        with open(file_path, 'a') as file:  # open a file to append the sentence
            file.write(text_to_append)  # write in a file to append a sentence
    except FileNotFoundError:
        print("File not found!")  # To except an error

def display_file_contents(file_path):  # defination to display file contents
    try:
        with open(file_path, 'r') as file:  # open a file
            content = file.read()  # open a file content
            print(content)
    except FileNotFoundError:  # except an error
        print("File not found!")

file_path = "sample.txt"  # file path
text_to_append = "\nThis is some additional text to append."  # to append a new sentence
append_to_file(file_path, text_to_append)  
print("Updated contents:")  # print the new line added to the text file
display_file_contents(file_path)  # display the content in the file
