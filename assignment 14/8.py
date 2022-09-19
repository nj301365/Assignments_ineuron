l=[0,5,3,6,7,1,4,5,1,6,7,3,4,8,6,3,6,2,7,4,0,4,8]
l.sort()
i=0
while i<len(l)-1:
    c=0
    while  i<len(l)-1 and l[i]==l[i+1]:
        c+=1
        i+=1
    c+=1
    print(l[i],":",c,"times")
    i+=1

if l[len(l)-1]!=l[len(l)-2]:
    print(l[len(l)-1],":",1,"times")
