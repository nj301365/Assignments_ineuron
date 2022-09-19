x=int(input("x="))
y=int(input("y="))
z=int(input("z="))
print("1. right angel triangle")
print("2. isosecles triangle")
print("3. eqilateral triangle")
choice=int(input())
match choice:
    case 1:
        if (x**2==(y**2)+(z**2) or (y**2)==(x**2)+(z**2)) or ((z**2)==(y**2)+(x**2)):
            print("triangle is right angled")
        else:
            print("not a right angle triangle")
    case 2:
        if (x==y or y==z) or x==z:
            print("isosceles triangel")
        else :
            print("not a isosceles triangel")
    case 3:
        if x==y==z:
            print("equiateral triangle ")
        else:
            print("not a equilateral triangle")
    case _:
        print("wrong input")
        
