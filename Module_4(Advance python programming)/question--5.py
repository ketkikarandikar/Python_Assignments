# Write a Python program to read a file line by line and store it into a list

def read_file_lines(file_path): # defination to read file line by line
    lines = []  # empty list
    try:
        with open(file_path, 'r') as file: # open the file
            for line in file:  
                lines.append(line.strip())  # Strip removes leading and trailing whitespaces including '\n' 
    except FileNotFoundError:
        print("File not found!")
    return lines

# Example usage:
file_path = "sample.txt"  
lines_list = read_file_lines(file_path)
print(lines_list)  # print the lines in a list
