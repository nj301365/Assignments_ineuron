my_set = {10, 20, 30, 40}
it = iter(my_set)

for _ in range(len(my_set)):
    print(next(it))
