def print_binary(n):
    if n > 1:
        print_binary(n // 2)
    print(n % 2, end="")

print_binary(10)  # Output: 1010
