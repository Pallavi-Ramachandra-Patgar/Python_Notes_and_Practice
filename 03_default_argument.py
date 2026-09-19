'''
Default Parameter Value:
We can have a value as defult as default argument in a function

if we specify name = "Stranger" in the line containig def, this value is used when 
no argument is passed'''

def goodday(name , ending = "Thankyou"):
    print(f"Good Day, {name}" )
    print(ending)
goodday("Pallavi","Thanks")

