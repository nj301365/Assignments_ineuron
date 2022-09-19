n = int(input())
k = 2
count = 0
while count < n:
    i = 2
    c = 0
    while i < k:
        if k % i == 0:
            c = c+1
            break
        i = i+1
    if c == 0:
        print(k, "is prime no.")
        count = count+1
    k = k+1
