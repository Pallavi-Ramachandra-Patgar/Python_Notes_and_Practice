'''Break : It is used to come out of the loop when encountered.It instructs the program to 
exit the loop now'''
#Example
for i in range(20):
    if(i==4):
        break #exit the loop right now
    print(i)  # o/p :0,1,2,3

'''Countinue : It use to stop the current iteration of the loop and continue with the next one.It 
instructs the Program to "skip this iteration'''
#Example
for i in range(20):
    if(i==4):
        continue #Skip this iteration
    print(i)  # o/p :0,1,2,3

'''Pass statment: It is a null statment in python.It instruct to "do nothing" '''
#Example
for i in range(10):
    pass
i = 0
while(i<5):
    print(i)
    i += 1