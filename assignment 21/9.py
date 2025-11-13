def print_multiples(n, number, current=1):
    if n > 0:
        print(number * current, end=" ")
        print_multiples(n-1, number, current + 1)

print_multiples(5, 3)  # first 5 multiples of 3
