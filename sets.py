#unordered unindexed collection
mySet = {"Nairobi", "Mombasa", "Kakamega"}
#Accessing items in a set
    # The items are unindexed - loop through the set

for item in mySet: print('item')

#You can't change item values for a set
#You can only addd more items using the add func (singular) & update (multiple)
mySet.add("Nakuru")
mySet.update("Molo", "Narok")
print(mySet)