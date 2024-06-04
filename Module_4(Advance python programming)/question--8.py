# Write a Python program to count the number of lines in a text file.

def count_lines(file_path):  # defination to count the lines in the text file
    line_count = 0  # start from
    try:
        with open(file_path, 'r') as file:  # open the file
            for line in file:
                line_count += 1  # count the line
    except FileNotFoundError:
        print("File not found!")
    return line_count

file_path = "sample.txt"  
number_of_lines = count_lines(file_path) # count the number of lines and store in the number_of_lines
print("Number of lines in the file:", number_of_lines)  # print the number of lines in the text file
