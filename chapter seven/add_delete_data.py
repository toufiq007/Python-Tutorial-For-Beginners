
# add and delete data form dictionaries



user_info = {
    'name' : 'Mostafiz',
    'age' : 20,
    'favourite_movie' : ['coco','terminator','matrix'],
    'favourite_songs' : ['forgive me','ei obelay'],
    'nickname' : ('lebu','manik','baba')
}


user_info['others'] = ['textile engnieering student at ptec']

# print(user_info)


# popped_item = user_info.popitem()
# print(popped_item)
# print(type(popped_item))



popped_item = user_info.pop('age')

print(popped_item)
print(type(popped_item))







# user_info['lang'] = ['javascript','python','html','css']

# print(user_info)

# pop_items = user_info.pop('age')
# print(pop_items)
# print(type(pop_items))

# print(user_info)
# popped_item  = user_info.pop('name')
# print(popped_item)
# print(type(popped_item))



popped_item = user_info.popitem()

# print(popped_item)
# print(type(popped_item))



# how to add data in dictionaries

user_info['fav_sports'] = ['football','cricket','badminton']
# print(user_info)

# for i in user_info.items():
#     print(i)



# how to remove data by using pop method


# pop_items = user_info.pop('favourite_movie')
# print(user_info)
# print(pop_items)
# print(type(pop_items))

# print(user_info)
# user_info.pop('age')
# print(user_info)






# remove data by using pop items method
# popitem method randomly removes a data form the dictionaries with keyvalues

# popitems returns the removes value in a tuples

# print(user_info)
popped_item = user_info.popitem()

# print(user_info)

# print(popped_item)
# print(type(popped_item))






