def even_numbers(n):
    for i in range(1, n+1):
        yield 2*i

for num in even_numbers(5):
    print(num, end=" ")
