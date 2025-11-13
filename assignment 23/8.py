def endless_primes():
    num = 2
    while True:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            yield num
        num += 1

prime_gen = endless_primes()
for _ in range(10):
    print(next(prime_gen), end=" ")
