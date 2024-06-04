# Write a Python program to write a list to a file. 

def write_list_to_file(file_path, my_list):  # Initialize the write list to file
    try:
        with open(file_path, 'w') as file:  # open the file
            for item in my_list:
                file.write(str(item) + '\n')  # write a string in new line
        print("List has been written to the file successfully!")  # print the list 
    except Exception as e:
        print("An error occurred:", e) # if the error occurs

file_path = "output.txt"  # Specify the path of the file to write the list
my_list = [1, 2, 3, 4, 5]  # list
write_list_to_file(file_path, my_list)  # write list to file
