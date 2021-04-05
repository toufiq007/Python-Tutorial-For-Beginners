
# in and iterations in python


user_info = {
    'name' : 'Mostafiz',
    'age' : 20,
    'favourite_movie' : ['coco','terminator','matrix'],
    'favourite_songs' : ['forgive me','ei obelay']
}


# for i in user_info.items():
#     print(i)

for i in user_info.items():
    print(i)
    print(type(i))



# user_info_items = user_info.items()
# print(user_info_items)


# for i in user_info:
#     print(user_info[i])


# for i in user_info.values():
#     print(i)


# for i in user_info:
#     print(i)


# for i in user_info.items():
#     print(i)

# print(user_info)


# check if key is exist in dictionary
# check key is this way under below

# if 'names' in user_info:
#     print('present')
# else:
#     print('not present')





# check if value is exist in dictionary  --> values method
# check value is this way under below

# if 'Mostafiz' in user_info.values():
#     print('yeah value is present')
# else:
#     print('sorry! value is not present')





# loop in dictionary

# for i in user_info:
#     print(i)

# for i in user_info:
#     print(i)




# values method
# you can print all the values on a dictionary by using values method
# exmple below


user_info_value = user_info.values()
# print(user_info_value)
# print(type(user_info_value))

# for i in user_info.values():
#     print(i)

# you can print all the value by this way also
# exmple below
# for i in user_info:
#     print(user_info[i])




# keys method
# you can print all the keys alos but default for loop print the keys on a dictionary by using values method
# exmple below

user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))



# for i in user_info:
#     print(i)





# items method it is the most usable method with dictionary
# items method prints the key and values also like a li



# for i in user_info.items():
#     print(i)
    



# user_info_items = user_info.items()
# print(user_info_items)
# print(type(user_info_items))

# for key, value in user_info.items():
#     print(f'key is {key} and value is {value} ')

# print(user_info.items())

# output look like below
# list = [('name', 'Mostafiz'), ('age', 20), ('favourite_movie', ['coco', 'terminator', 'matrix']), ('favourite_songs', ['forgive me', 'ei obelay'])]












