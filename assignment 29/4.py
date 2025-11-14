cities = ['New York', 'London', 'Tokyo', 'Paris', 'Sydney']
file_name = 'cities.txt'

with open(file_name, 'w') as file:
    for city in cities:
        file.write(city + '\n')

print(f"City names have been written to {file_name}")
