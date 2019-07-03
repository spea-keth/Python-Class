'''



Python data collection
1. List: collection which - is ordered & changeable
                          - allows duplicates
2. Tuple: collection which - is ordered & unchangeable
                           - allows duplicates
3. Set: collection which - is unordered & unindexed
                         - allows no duplicates
4. Dictionaries: collection which - is unordered, changeable & unindexed
allows duplicates


##List
    # Syntax
listname = ['Paul', 'Mikey', 'Mary', 'Laura', 'Steven', 'Esther']
    #Accessing
print(listname[1])
print("I am " + listname[1] + ".")

m = listname[1]
print("I am {}".format(m))

#looping

for name in listname:
    print("My name is {}".format(name) + ".")

#Checking if an item exists u=in a list
if 'Lara' in listname:
    print("Lara is present in the list.")
print(len(listname))

#listname.append('item')
listname.append('Bob')
print(listname)

listname.insert(0,'Janet')
print(listname)
'''
'''
ASS
remove() removes a specified item in the list
    listname.remove(itemname) e.g "Bob"
pop() - removes last item (if parameter is blank) but one can also specify index
    listname.pop()
del() - removes specific indexed item from list
    del listname [}
clear() erase whole list
'''
'''
for name in listname:
    print(name)

listname.remove("Mary")
print("#######################\n\n" + str(listname))

listname.pop()
print("#######################\n\n" + str(listname))


del listname[4]
print("#######################\n\n" + str(listname))

#Creating an empty list
animal = []
animal = list()

people = list(("Item1", "Item2"))
movies = ['Game of Thrones', ['John', 'Mary', 'Aria']]
print(movies[1][2])

alphabet = list()
#alphabet.insert("a", "b", "c")
#print(alphabet
'''
