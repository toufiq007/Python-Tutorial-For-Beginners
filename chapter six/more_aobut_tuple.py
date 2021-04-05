
# looping in tuple
# tuple with one element
# tuple without parenthesis 
# tuple unpacking
# list inside tuple
# some functions that you can use with tuple


# looping in tuple

mixed = [1,2,3,4,5,6,7,8]

# for loop
# for i in mixed:
#     # print(i)



# while loop
# i = 1
# while i <= len(mixed):
#     print(i)
#     i += 1





# tuple with one element

# you must give a comma after declare a one element otherwise it is counting string or integers
name = ('limon',)
# print(type(name))




# tuple without parenthesis

name = 'limon', 'salman','tamim','rudro','konika'
# print(type(name))





# tuple unpacking

name = ('limon','salman','tamim')

name1,name2,name3 = (name)  # this is called tuple unpacking.you can store them any variable

# print(name1)
# print(name2)
# print(name3)




# list inside tuple
# you can store a list inside a tuple and do any operations with the list

name = ('limon','tamim',['i am well','is it ok','landscape'])

# print(name[2])
# print(name[2].pop())

name[2].pop()
name[2].append('i am back')
# print(name)





# some functions that you can use with tuple
# sum() ,, min() ,, max() ,, count()

# print(sum(mixed))
# print(min(mixed))
# print(max(mixed))


# using count and length method

name = ('limon','salman','tamim','limon','rudro','atiqur','limon')

print(name.count('limon'))
print(len(name))






