n=int(input())
i=0
a=0
b=1
print(a,b,sep=" ")
while i<n-2:
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    i=i+1