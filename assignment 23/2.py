def odd_numbers(n):
    for i in range(n):
        yield 2*i + 1

for num in odd_numbers(5):
    print(num, end=" ")
