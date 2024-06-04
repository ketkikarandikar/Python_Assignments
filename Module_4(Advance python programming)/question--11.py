# Write a Python program to copy the contents of a file to another file.

def copy_file(sample_file, example_file):  # define the file to copy
    try:
        with open(sample_file, 'r') as sample:  # open the file to be read
            with open(example_file, 'w') as example:  # open the file to write
                for line in sample:  
                    example.write(line)  # write in the file
        print("File copied successfully!")  
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred:", e)

sample_file = "sample.txt"  
example_file = "example.txt"  
copy_file(sample_file, example_file)
