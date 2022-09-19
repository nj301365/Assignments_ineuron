n=int(input())
l=[]
while n>0:
    if n%2==0:
       l.append(0)
    else:
        l.append(1)
    n=n//2
l1=l[::-1]
for i in l1:
    print(i,end="")
   