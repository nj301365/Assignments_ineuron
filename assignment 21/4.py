def print_odd_reverse(n, current=1):
    if n > 0:
        print_odd_reverse(n-1, current + 2)
        print(current, end=" ")

print_odd_reverse(5)
