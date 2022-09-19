s1=input("s1:")
s2=input("s2:")
match " ":
    case " " if s1>s2:
        print("s1 comes first in dictionary")
    case " " if s1<s2:
        print("s2 comes first in dictionary")
    case " " if s1==s2:
        print("both string are identical")