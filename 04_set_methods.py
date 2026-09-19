s = {1,5,32,54,5,5,5,"Pallavi"}
print(s, type(s))

'''Properties of sets:
Sets are unoredered ==> Element's order doesn't matter.`
Sets are unindexed ==> Cannot access elements by index.
There is no way to change items in sets.
Sets cannot contain duplicate values.

Operation of sets:'''
s={1,8,2,3}
a = len(s)      #Returns 4, the length of the set.
print(a)   #o/p 4

b = s.remove(1) #Updated the set s and removes 8 from s.
print(s)     #o/p None

g = s.add(25) #It will add 25 in the set s.
print(s)   #o/p {8, 25, 2, 3}

e = s.union({8,15}) #Returns new set with all item from both sets
print(s.union(e))   #o/p {2, 3, 8, 15, 25}

f = s.intersection({8,11}) #Returns a set which contains only item in both sets.
print(s.intersection(f))   #o/p {8}

c = s.pop()      #Removes an arbitrary element from the set and return the element removed.
print(s)   #o/p {25, 2, 3}

d = s.clear()    #Empties the set s.
print(s)   #o/p set()















