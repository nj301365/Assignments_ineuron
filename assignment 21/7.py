def print_squares(n):
    if n > 0:
        print_squares(n-1)
        print(n**2, end=" ")

print_squares(5)
