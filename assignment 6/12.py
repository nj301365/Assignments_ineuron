x=complex(int(input("enter a real part:")),int(input("enter imaginary part:")))
print(type(x))
print("real part big" if x.real>x.imag else "img part big")