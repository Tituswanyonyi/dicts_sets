#DICTIONARIES
foods = {
    'Lunch': ['Banana', 'Rice'],
    'Supper': 'Fish' 
}
print(foods)
print(type(foods))
print('')
#Accessing items in dictionary
print(foods['Lunch'])
print(foods['Supper'])
foods['Supper']= 'Shrimps'

print(foods)
print('')
#Adding items
foods.update({'Breakfast': 'Tea'})
print(foods)
print ('')

#Clearing and deleting disctionaries
foods.clear()
print(foods)

del foods
#print (foods)
print('')

#copying dictionaries
print('')
newdict= {'a':30, 'b':'Wire', 'c':[3, 7]}
print(newdict)
newdictcopy = newdict.copy()
print(newdictcopy)
copy3 = dict(newdictcopy)
print(copy3)
print('')

#SETS CODES
elements = {4, 'James', 4.5}
print(elements)
nums = set((5,8,12))
print(nums)
print(type(nums))
print ('')
#check if an item is in a set
print(5 in nums)
nums.add(817)
print (nums)
morenums = {33, 87, 90}
nums.update(morenums)
print(nums)
print('')

#Merging two sets (use union function)
alpha = {4,8,9}
omega = {6,3,76}
merger =alpha.union(omega)
print(merger)