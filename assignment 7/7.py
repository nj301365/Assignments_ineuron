num=int(input("enter no."))
match num:
    case num if num>0:
        print("greaeater than zero")
    case num if num<0:
        print("less than zero")
    case num if num==0:
        print("number is zero")