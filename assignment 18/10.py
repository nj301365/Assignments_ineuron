sample_dict = {
    'C': 92,
    'Java': 66,
    'Python': 85
}

# Initialize variables to store the minimum value and corresponding key
min_value = None
min_key = None

# Loop through dictionary items
for key, value in sample_dict.items():
    if min_value is None or value < min_value:
        min_value = value
        min_key = key

print("Key with lowest value:", min_key)
