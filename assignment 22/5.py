def sum_cubes(n):
    if n == 0:
        return 0
    return n**3 + sum_cubes(n-1)

print(sum_cubes(5))  # Output: 225 (1+8+27+64+125)
