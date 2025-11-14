# Define the source and destination file paths
source_file = 'example.txt'
destination_file = 'example_copy.txt'

# Open the source file in read mode and the destination file in write mode
with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
    # Read the content of the source file
    content = src.read()
    
    # Write the content to the destination file
    dest.write(content)

print(f"Content has been copied from {source_file} to {destination_file}")
