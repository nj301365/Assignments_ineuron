def print_even_reverse(n, current=2):
    if n > 0:
        print_even_reverse(n-1, current + 2)
        print(current, end=" ")

print_even_reverse(5)
