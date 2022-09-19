a=int(input('a:'))
b=int(input('b:'))
k=input()
match k:
    case "add":
        print(a+b)
    case "sub":
        print(a-b)
    case "div":
        print(a//b)
    case "mul":
        print(a*b)
    case _:
        print("g")
