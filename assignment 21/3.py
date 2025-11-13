def print_odd(n, current=1):
    if n > 0:
        print(current, end=" ")
        print_odd(n-1, current + 2)

print_odd(5)
