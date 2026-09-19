''' A function can accept some value it can work with.We can put these value in the parenthesis'''
def goodday(name,ending):
    print("Good day," +name)
    print(ending)
 
goodday("Pallavi","Thankyou")
goodday("Shivam","Thankyou")
goodday("Sampriya","Thanks")
'''o/p 
Good day,Pallavi
Thankyou
Good day,Shivam
Thankyou
Good day,Sampriya
Thanks'''

def greatday(name,ending):
    print("Great day," +name)
    print(ending)
    return"Done"

a = greatday("Pallavi","Thankyou")
print(a)
'''o/p 
Great day,Pallavi
Thankyou
Done'''

