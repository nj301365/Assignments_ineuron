# Original tuple of tuples
tuple1 = (('a', 21), ('b', 37), ('c', 11), ('d', 29))

# Sort by the second item of each inner tuple
sorted_tuple = tuple(sorted(tuple1, key=lambda x: x[1]))

# Print the result
print("Sorted tuple:", sorted_tuple)
