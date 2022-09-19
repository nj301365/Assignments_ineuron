a=int(input("enter number:"))
b=int(input("enter number:"))
c=int(input("enter number:"))

qe="ax^2+bx+c"
d=(b*b)-(4*a*c)
if d>0:
    print("two real and distanct roots")
elif d==0:
    print("equal roots")
elif d<0:
    print("imaginary roots")