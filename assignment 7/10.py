a=input("your fav color")
l=["Yellow","Blue","Orange","White","Black","Red"]

for i in l:
    if i in a:
        k=i
        break
else:
    k="other"
match k:
    case "Yellow":
        print("Monday")
    case "Blue":
        print("Tuesday")
    case "Orange":
        print("Wednesday")
    case "White":
        print("Thursday")
    case "Black":
        print("Friday")
    case "Red":
        print("Saturday")
    case "other":
        print("Sunday")
