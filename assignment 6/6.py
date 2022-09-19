n=int(input("enter number:"))

s=str(n)    #first approach
print("3 digit no." if len(s)==3 else "not a 3 digit no.")

 #second approach
count=0
while n>0:
    count=count+1
    n=n//10

if count==3:
    print("three digit no.")
else:
    print("not a three digit no.")