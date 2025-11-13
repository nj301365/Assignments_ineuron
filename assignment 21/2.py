def print_natural_reverse(n):
    if n > 0:
        print(n, end=" ")
        print_natural_reverse(n-1)

print_natural_reverse(5)
