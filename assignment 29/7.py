import keyword

file_name = 'example.py'  
keyword_count = 0

with open(file_name, 'r') as file:
    code = file.read()
    for word in keyword.kwlist:
        keyword_count += code.count(word)

print(f"Number of Python keywords in {file_name}: {keyword_count}")
