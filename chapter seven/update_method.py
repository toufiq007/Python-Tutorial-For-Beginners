
# point to be noted

# update method is basically used to add a dictionary by another dictionary

# if second dictionary have a key that is already exist in first dictionary then it is'not created a new key it update the previous one with value

# update method can't return anything so you can't store update method in a variable


user_info = {
    'name' : 'Mostafiz',
    'age' : 20,
    'favourite_movie' : ['coco','terminator','matrix'],
    'favourite_songs' : ['forgive me','ei obelay'],
    'nickname' : ('lebu','manik','baba')
}



more_info = {
    'hobbies' : ['singing','programming','travelling'],
    'name' : 'Toufiq limon'
}

user_info.update()
print(user_info)
# you got output None
# update_item = user_info.update(more_info)
# print(update_item)









