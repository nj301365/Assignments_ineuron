s=input("enter something:")

length_of_string=len(s)
match length_of_string:
    case length_of_string if length_of_string==1:
        print("single valued string")
    case length_of_string if length_of_string>=1:
        print("multi valued string")
    case _:
        print("invalid input")
