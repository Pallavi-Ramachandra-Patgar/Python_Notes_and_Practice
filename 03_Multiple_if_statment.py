a = int(input("Enter your age: "))

# if statment no:1
if(a%2==0):
    print("Even")
#End of if statment 1

#if statment no:2
if(a>=18):
    print("Your are above the age of concent")
elif(a<0):
    print("You are entering the an invalid age")
elif(a==0):
    print("You are entering 0 which is not a valid age")
else:
    print("Your are below the age of concent")