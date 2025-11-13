def max_of_four(a, b, c, d):
    max_num = a
    for num in [b, c, d]:
        if num > max_num:
            max_num = num
    return max_num

print("Maximum:", max_of_four(10, 25, 15, 20))
