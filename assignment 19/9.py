def in_range(num, start, end):
    if start <= num <= end:
        print(f"{num} is in range {start}-{end}")
    else:
        print(f"{num} is not in range {start}-{end}")

in_range(10, 5, 15)
in_range(20, 5, 15)
