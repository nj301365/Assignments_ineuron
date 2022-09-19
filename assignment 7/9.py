year = int(input("year:"))
match year:
    case year if year%4==0 and year%100!=0 and year%400!=0:
        print("non century leap year")
    case year if year%4==0 and year%100==0 and year%400==0:
        print("century leap year")
    case year if year%4==0 and year%100==0 and year%400!=0:
        print("century non leap year")
    case year if year%4!=0 :
        print("non century non leap year")