additional_cities = ['Berlin', 'Amsterdam', 'Rome']
file_name = 'cities.txt'

with open(file_name, 'a') as file:
    for city in additional_cities:
        file.write(city + '\n')

print(f"Additional city names have been appended to {file_name}")
