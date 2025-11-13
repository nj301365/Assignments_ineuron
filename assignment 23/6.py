def primes(n):
    count = 0
    num = 2
    while count < n:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            yield num
            count += 1
        num += 1

for p in primes(5):
    print(p, end=" ")
