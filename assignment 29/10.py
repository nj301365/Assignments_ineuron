import pickle

file_name = 'bookfile.pkl'

# Load the data using pickle
try:
    with open(file_name, 'rb') as file:
        books = pickle.load(file)
        print("Extracted Book Data:")
        for book, price in books.items():
            print(f"{book}: ${price}")
except FileNotFoundError:
    print(f"{file_name} does not exist.")
