#check wheather a year is leap year or not
year = int(input("enter a year"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            year = "leap year"
        else:
            year = "not leap year"
    else:
        year = "leap year"
else:
    year = "not leap year"

# main approach
month = int(input())
if month == 4 or month == 6 or month == 9 or month == 11:
    print(30)
elif month == 2:
    if year == "leap year":
        print(29)
    else:
        print(28)
else :
    print(31)
