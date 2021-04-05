
# map functions in python

number = [1,2,3,4,5]
# square = list(map(lambda x : x**2,number))

# for i in square:
#     print(i)



number = list(range(1,10))

cube_func = list(map(lambda x: x**3,number))
print(cube_func)



# create a list with general expression

# def square(x):
#     return x**2

# print(square(4))




# create a list with map function

# sqr = lambda x: x**2
# square = list(map(sqr,number))

# square = list(map(lambda x : x**2, number))
# print(square)



# create a list of square number with list comprehension

# def square(x):
#     return [i**2 for i in x]

# print(square(number))



# def square(x):
#     new_list = []

#     for i in number:
#         new_list.append(i**2)
#     return new_list

# print(square(number))



# you can use loop in map function by only one time but when you convert map function in list then you should able to use loop infinity times with map function




names = ['limon','toufiq','tamim']

# find_length = map(len,names)
# find_length = list(map(len,names))

# for i in find_length:
#     print(i)


# for j in find_length:
#     print(j)


# names = list(map(len,names))
# print(names)


# for i in names:
#     print(i)