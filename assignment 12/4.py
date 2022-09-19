x1=int(input("x1:"))
x2=int(input("x2:"))
for i in range(x1,x2+1):
    n=2
    while n<i:
        if i%n==0:
            print(i,":not prime")
            break
        n=n+1
    else:
        print(i,":prime number")