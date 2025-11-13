def sum_squares(n):
    if n == 0:
        return 0
    return n**2 + sum_squares(n-1)

print(sum_squares(5))  # Output: 55 (1+4+9+16+25)
