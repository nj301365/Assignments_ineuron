def sum_odd(n):
    if n == 0:
        return 0
    return (2*n - 1) + sum_odd(n-1)

print(sum_odd(5))  # Output: 25 (1+3+5+7+9)
