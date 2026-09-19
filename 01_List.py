# List are containers to store a set of values of any data type
# List are mutable (Mutable: where we can change, add n remove any data )

friends = ["Apple","Orange", 15, 2000, False,"Ramachandra"]
print(friends[0]) #o/p :Apple 

# if want to replace Apple to Banana 
friends[0]="Banana"
print(friends[0]) #o/p: Banana

#slicing
print(friends[0:4]) #o/p: ['Banana', 'Orange', 15, 2000]