n=int(input())

k=n+1
while k:
    i=2
    c=0
    while i<k:
        if k%i==0:
            c=c+1
            break
        i=i+1
    if c==0:
        print(k,"is prime no.")
        break
    k=k+1
