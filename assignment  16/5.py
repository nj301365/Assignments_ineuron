# Ask the user how many elements they want in the tuple
n = int(input("Enter the number of elements: "))

# Create an empty list to collect elements
items = []

# Take user input for each element
for i in range(n):
    value = input(f"Enter element {i+1}: ")
    items.append(value)

# Convert the list to a tuple
t1 = tuple(items)

# Assume all elements are same initially
all_same = True

# Compare each element with the first one
for item in t1:
    if item != t1[0]:
        all_same = False
        break

# Display result
if all_same:
    print("All items in the tuple are the same.")
else:
    print("Not all items in the tuple are the same.")
