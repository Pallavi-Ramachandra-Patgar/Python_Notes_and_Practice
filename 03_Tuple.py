#Tuple is Immutable, In tuple we can't change 
a=(1,2,3,4,)
print(type(a)) #o/p:<class 'tuple'>

a=(1,2,3,4,"Palla","Ramchandra")
print(type(a)) #o/p:<class 'tuple'>

#METHODS OF TUPLE:
#Count(): Returns the number of times a specified value appears in the tuple.
no = a.count(4)
print(no) #o/p: 1 

#index():Return the index of the first occurence of a specified value in the tuple.Raises "valueerror" if the value is not found
no = a.index(4)
print(no) #o/p: 3

#Concatination: Tuple can be concatinated using '+' operator
tuple1 = (1,2,3,4)
tuple2 = (5,6,7,8)
concatenated = tuple1+tuple2
print(concatenated) #o/p: (1, 2, 3, 4, 5, 6, 7, 8)

#Repetition: Tuple can be Repeated using '*' operator
my_tuple = (1,2,3,4)
repeated = my_tuple * 3
print(repeated) #o/p:(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

#Membership: We can check if an item exists in a tuple using the 'in' keyword
my_tuple=(1,2,3,4)
print(2 in my_tuple) # o/p : True
print(5 in my_tuple) # o/p : False

