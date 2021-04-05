
# when you add something on the list then you have 3 method

# add method
# append()
# extend()
# insert()


# remove method
# pop()  ==> defalut remove data from the last in a list
# remove()
# del method

# pop() and del method works with the index of specific index of the data and remove() works the specific name of the data


fruits = ['apple','orange','banana']
print(fruits)


# print(fruits)
# fruits.pop()
# print(fruits)


# using pop method you can also remove the specific data form a list by using index of the current data

# like this

# fruits.pop(2)
# print(fruits)



# you can remove data without knowing the exact value of index by using remove method

# fruits.remove('orange')
# print(fruits)




# by using del you can delete the current data what should you want to delete

# del fruits[1]
# print(fruits)



fruits2 = ['mango','strawberry','bean']
print(fruits2)


fruits.append(fruits2)
print(fruits)



fruits.extend(fruits2)
print(fruits)








