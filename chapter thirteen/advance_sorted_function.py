
# advance sorted fucntion in python 

fruits = ['mango','grape','apple']
# fruits.sort()
# print(fruits)

fruits = ('mango','grape','apple') # tuples are inmuttuable 
# sorted method can't change the main tuple it make a new list and append the items to new list
# sorted(fruits)
# print(sorted(fruits))

fruits = {'mango','grape','apple'}
# sorted method took the set and make a new list and sort the items and append to new list

# print(sorted(fruits))


bikes = [
    {'model' : 'yahmama rx100', 'price' : 70000},
    {'model' : 'yahmama Fzs', 'price' : 270000},
    {'model' : 'yahmama R1-5', 'price' : 570000}
]

sorted_bike = sorted(bikes,key= lambda items: items.get('price'),reverse=True)

print(sorted_bike)


