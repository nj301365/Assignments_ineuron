import pickle

# Sample book data in dictionary form
books = {
    'The Great Gatsby': 10.99,
    '1984': 8.99,
    'To Kill a Mockingbird': 7.99,
    'Moby Dick': 12.50
}

file_name = 'bookfile.pkl'

# Store the dictionary data using pickle
with open(file_name, 'wb') as file:
    pickle.dump(books, file)

print(f"Book data has been stored in {file_name}")
