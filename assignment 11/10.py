n=int(input())

l=[]
while n>0:
    if n%8==0:
       l.append(0)
    elif n%8==1:
        l.append(1)
    elif n%8==2:
        l.append(2)
    elif n%8==3:
        l.append(3)
    elif n%8==4:
        l.append(4)
    elif n%8==5:
        l.append(5)
    elif n%8==6:
        l.append(6)
    elif n%8==7:
        l.append(7)
    
    n=n//8
l1=l[::-1]
for i in l1:
    print(i,end="")