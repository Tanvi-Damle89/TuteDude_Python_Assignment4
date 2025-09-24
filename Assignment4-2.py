# Task 2: Write and Append Data to a File

# Step 1: Writing user input to the file
user_input = input("Enter some text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")
print("Data written to 'output.txt' successfully!")

# Step 2: Appending more data to the file
additional_input = input("Enter some text to append to the file: ")

with open("output.txt", "a") as file:
    file.write(additional_input + "\n")
print("Additional data appended to 'output.txt' successfully!")

# Step 3: Reading and displaying the final content
print("\nFinal content of 'output.txt':")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
