num=int(input("enter a no."))
match num:
    case num if num%2==0:
        print("Saurabh Shukla")
    case num if  num<0 and num%2==1:
        print("Prateek Jain")
    case num if  num%2==1:
        print("Aditya Choudhary ")
