x=int(input("x:"))
y=int(input("y:"))
z=min(x,y)
i=2
c=0
while i<=z:
    if x%i==0 and y%i==0:
        c=c+1
        print("not coprime")
        break
    i=i+1
if c==0:
    print("coprime no.")