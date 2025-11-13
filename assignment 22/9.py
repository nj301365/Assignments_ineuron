def print_octal(n):
    if n > 7:
        print_octal(n // 8)
    print(n % 8, end="")

print_octal(65)  # Output: 101
