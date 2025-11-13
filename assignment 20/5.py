def min_of_three(a, b, c):
    minimum = a
    if b < minimum:
        minimum = b
    if c < minimum:
        minimum = c
    return minimum

print(min_of_three(10, 5, 15))
