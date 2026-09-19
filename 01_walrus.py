'''The walrus operator(:=):It allows u to variable as part of an expression this 
operator named for this its resembleance to the eyes and tusks of a walrus,
is officially called the assignment expression'''
if(n:= len([1,2,3,4,5]))>3:
    print(f"List is too long ({n} elemenmts, expected <=3)")

#o/p:List is too long (5 elemenmts, expected <=3)

'''In this example,n is assigned the value of len([1,2,3,4,5]) and then used in 
the comparison within the if statement'''