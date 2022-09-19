a=int(input())
b=int(input())
while 1:
    if a==0 or b==0:
        break
    z=max(a,b)
    if z==a:
        a=a-b
    else:
        b=b-a
print(a if b==0 else b)