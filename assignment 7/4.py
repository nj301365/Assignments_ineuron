age=int(input('enter an number'))
match age:
    case age if age<10:
        print("kid:",age)
    case age if age>=10 and age<20:
        print("teen:",age)
    case age if age>=20 and age<40:
        print("young:",age)
    case age if age>=40 and age<60:
        print("experienced:",age)
    case age if age>=60:
        print("senior citizen:",age)
