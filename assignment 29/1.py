# Open the file
file_name = 'example.txt'

# Open the file in read mode
file = open(file_name, 'r')

# Check if the file is closed or not
is_closed = file.closed

# Check the file opening mode
file_mode = file.mode

# Check if the file is read-only based on its mode
is_read_only = 'r' in file_mode or '+' not in file_mode  # 'r' mode means read-only, '+' means read-write

# Print file status
print(f"File Name: {file_name}")
print(f"Is the file read-only? {'Yes' if is_read_only else 'No'}")
print(f"Is the file closed? {'Yes' if is_closed else 'No'}")
print(f"File opening mode: {file_mode}")

# Close the file after checking
file.close()
