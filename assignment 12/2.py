x=int(input("enter a number:"))
n=2
while n<x:
    if x%n==0:
     print("not prime")
     break
    n=n+1
else:
    print("prime number")