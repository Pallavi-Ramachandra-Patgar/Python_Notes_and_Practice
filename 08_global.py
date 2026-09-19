a = 89 #Global variable
def fun():
    a = 3
    print(a)

fun()
print(a)

'''o/p : 
3
89'''

# Enumarate:
l = [1,2,3,4,5,6]

"""index = 0
for item in l:
    print(f"The item number at index {index} is {item}")
    index +=1"""
    
#This can be simplified using enumerate function 

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")

'''o/p:
The item number at index 0 is 1
The item number at index 1 is 2
The item number at index 2 is 3
The item number at index 3 is 4
The item number at index 4 is 5
The item number at index 5 is 6'''

#List_Comprehensions:
my_list = [1,2,3,4,5]

'''squaredlist = []
for item in my_list:
    squaredlist.append(item*item )'''

#using list_comprehensions

squaredlist = [i*i for i in my_list]
print (squaredlist)
'''o/p:
[1, 4, 9, 16, 25]'''