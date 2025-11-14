# Ask user for input and write to 'myfile.txt'
file_name = 'myfile.txt'

with open(file_name, 'w') as file:
    user_input = input("Enter text to store in the file: ")
    file.write(user_input)

print(f"Text has been written to {file_name}")
