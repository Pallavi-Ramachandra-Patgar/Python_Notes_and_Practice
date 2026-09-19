friends = ["Apple","Orange", 15, 2000, False,"Ramachandra"]
print(friends)

friends.append("Pallavi") # append is a method used to insert the data at the end of the list
print(friends) # o/p : ['Apple', 'Orange', 15, 2000, False, 'Ramachandra', 'Pallavi'] here Pallavi is added in the last due to using append method

'''Diffrence between list and string
STRING :In string if u use any method it will not change but it gives new value bcz it is immutable
LIST   :In List if u8 add any method list will be change bcz it is mutable'''

'''SOME METHODS OF LIST'''
#Sort : This method is used to give output in correct order which means in increasing order
l1 = [1,2,7,4,3,6,5]
l1.sort()
print(l1) #o/p: [1,2,3,4,5,6,7]

#Reverse : used to reverse 
l1 = [1,2,7,4,3,6,5]
l1.reverse()
print(l1) #o/p: [5, 6, 3, 4, 7, 2, 1]

#Insert : used to to add new item in middle 
l1 = [1,2,7,4,3,6,5]
l1.insert(3,15) #Insert 15 such that it's index in the list is 3
print(l1) #o/p: [1, 2, 7, 15, 4, 3, 6, 5]

#Pop:used to delete or remove  item in list 
l1 = [1,2,7,4,3,6,5]
l1.pop(3) #Delete the element which present in the index 3 and return it's value
print(l1) #o/p: [1, 2, 7, 3, 6, 5]

#remove:used to remove item from list 
l1 = [1,2,7,4,3,6,5]
l1.remove(3) #remove the element 3 from list
print(l1) #o/p: [1, 2, 7, 4, 6, 5]
