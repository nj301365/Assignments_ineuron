#first method
x=int(input("enter a 3 digit number:"))
s=str(x)
print(s[0])

#second method
x=int(input("enter a 3 digit number:"))
while x>=10:
    x=x//10
print(x)