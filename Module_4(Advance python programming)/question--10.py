# Write a Python program to write a list to a file. 

def write_list_to_file(file_path, my_list):
    try:
        with open(file_path, 'w') as file:
            for item in my_list:
                file.write(str(item) + '\n')
        print("List has been written to the file successfully!")
    except Exception as e:
        print("An error occurred:", e)

# Example usage:
file_path = "output.txt"  # Specify the path to the file where you want to write the list
my_list = [1, 2, 3, 4, 5]  # Replace this with the list you want to write
write_list_to_file(file_path, my_list)
