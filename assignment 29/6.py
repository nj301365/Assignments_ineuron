search_city = 'Paris'
file_name = 'cities.txt'

with open(file_name, 'r') as file:
    cities = file.readlines()

if any(search_city in city for city in cities):
    print(f"{search_city} is in the list.")
else:
    print(f"{search_city} is not in the list.")
