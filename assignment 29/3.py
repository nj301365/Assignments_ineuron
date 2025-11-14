# Read and display content of 'myfile.txt'
file_name = 'myfile.txt'

try:
    with open(file_name, 'r') as file:
        content = file.read()
        print(f"Content of {file_name}:")
        print(content)
except FileNotFoundError:
    print(f"{file_name} does not exist.")
