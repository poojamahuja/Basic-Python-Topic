# creating a list
myIntegerList = [9, 4, 3, 2, 8]
myFloatList = [2.0, 9.1, 5.9, 8.123432]
myCharList = ['p', 'y', 't', 'h', 'o', 'n']
myStringList = ["Hello", "Python", "Ok done!"]

# creating a list from another list
# complete copy
myNewList = myStringList
print (myNewList);
# copying only some list elements - first two
myNewList = myStringList[0:2]
print (myNewList);

# using range() function to create a list
myList1 = range(5)
print (myList1);

# APPEND list elements
emptyList = []
emptyList.append('The Big Bang Theory')
emptyList.append('F.R.I.E.N.D.S')
emptyList.append('How I Met Your Mother')
emptyList.append('Seinfeld')
print (emptyList);

# find number of elements in a list
print (len(emptyList));

# accessing using index - 0, 1, 2, 3
print (emptyList[1]);


#Iterating over a List
# Let's start by defining a list
myList = ['Last Of Us', 'Doom', 'Dota', 'Halo', ' ']
print (myList)

# using for loop
for x in myList:
  print (x)
  
# using while loop
i = 0
while i < len(myList):
  print (myList[i])
  i+=1

# Deleting the List Item
myList = ['zero', 'one', 'two', 'three', 'four', 'five']
print (myList)

# delete element using del keyword
del myList[1]
print (myList)

# remove element using remove method
myList.remove('two')
print (myList)

# pop an element out of the list
myList.pop(2)
print (myList)


# Insert, Reverse and Sort a List
# Inserting new list item
myList = ['Python', 'C++', 'Java', 'Ruby', 'Perl']
# inserting at a defined position - 1(index)
myList.insert(1, 'JavaScript')
print (myList)

# Reverse a List
myList.reverse()    # this returns None
print (myList)

# Sort a List
myList.sort()
print (myList)