# Task 1: Read a File and Handle Errors

try:
    # Attempting to open the file
    with open("sample.txt", "r") as file:
        print("File Content:\n")
        for line in file:
             print(line.strip())  # strip() removes any extra newline characters
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist. Please create the file and try again.")
