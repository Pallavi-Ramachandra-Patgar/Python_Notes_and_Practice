marks ={
    "Pallavi": 50,
    "Gaurav" : 48,
    "Shivam" : 49,
    "Sahil"  : 47
}



'''Methods Of Dictionary:'''
#.item():Returns a list of (key,value)tuples
print(marks.items()) 

#o/p :([('Pallavi', 50), ('Gaurav', 48), ('Shivam', 49), ('Sahil', 47)])

#.keys():Return a list containing dictionary's key
print(marks.keys()) 
#o/p:(['Pallavi', 'Gaurav', 'Shivam', 'Sahil'])

#.values():Return a list containing dictionary's values
print(marks.values())
#o/p:([50, 48, 49, 47])

#.update:Updates the dictionary with supplied key-value pairs.
marks.update({"Shivam":50,"Suraj":49})
print(marks)
#o/p: {'Pallavi': 50, 'Gaurav': 48, 'Shivam': 50, 'Sahil': 47, 'Suraj': 49}

#.get:Returns the vale of the specified keys
print(marks.get("Shraddha")) #o/p : None
print(marks.get("Gaurav")) #o/p : 48

#.pop:Removes the specified key and returns the corresponding value.
#     if the key is notfound,'default' is returned if provided,otherwise 'KeyError' is raised.


#.popitem():Removes and returns a pair from the dictionary.Pairs are returned in LIFO(last-in,first-out)

'''Note:if u use square bracket insted of bracket 
        u will get error if that perticular value is not present u will get Error
        eg:print(marks.get["Sahil"]) #o/p : Error
        similarly if u use bracket insted of square bracket u will get None
        eg:print(marks.get("Sahil")) #o/p : None'''
