# Write a Python program to copy the contents of a file to another file.

def copy_file(sample_file, example_file):
    try:
        with open(sample_file, 'r') as sample:
            with open(example_file, 'w') as example:
                for line in sample:
                    example.write(line)
        print("File copied successfully!")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred:", e)

# Example usage:
sample_file = "sample.txt"  # Replace "source.txt" with the path to the source file
example_file = "example.txt"  # Replace "destination.txt" with the path to the destination file
copy_file(sample_file, example_file)
