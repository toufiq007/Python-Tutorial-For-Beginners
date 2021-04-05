# pass function as a arguemnts

def square(x):
    return x**2


s = square

l = [1,2,3,4,5]

# print(list(map(s,l)))  # map function takes a fucntion and takes a iterable 



# breaking the map function to see how the map fucntion works

# def my_map(func,l):
#     new_list = []
#     for i in l:
#         new_list.append(func(i))
#     return new_list


# print(my_map(lambda a: a**3,l))


# def my_map(func,l):
#     return [func(i) for i in l]


# print(my_map(lambda a: a**4,l))

def cube(x):
    return x**3


def my_map(func,l):
    new_list = []
    for i in l:
        new_list.append(func(i))
    return new_list

mapping = my_map(square,l)

print(mapping)



mapping = map(lambda x: x**3,l)
print(list(mapping))