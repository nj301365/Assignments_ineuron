
for i in range(2,100):
    n=2
    while n<i:
        if i%n==0:
            print(i,":not prime")
            break
        n=n+1
    else:
        print(i,":prime number")