
personal_info = {}



# name = input('Enter your name :')
# age = input('Enter your age :')
# fav_sports = input('Enter your favourite sports by separating them comma : ').split(',')
# fav_language = input('Enter your favourite language by separating them comma : ').split(',')




# personal_info['name'] = name
# personal_info['age'] = age
# personal_info['fav_sports'] =fav_sports
# personal_info['fav_language'] =fav_language



# print(personal_info)

# you can print 2 way
# one is
# for i in personal_info:
#     print(f' {i} : {personal_info[i]} ')

# another is
# for key, value in personal_info.items():
#     print(f' {key} : {value} ')







user_info ={
    'name' : 'limon',
    'age' : 20,
    'hobby' : 'programming',
    'lang' : ['javascript','python'],
    'tuple' : ('salman','tamim') 
}

print(user_info)
another_lang = ['html','css','bootstrap']

user_info['lang'].extend(another_lang)
print(user_info)



# pop_items = user_info.popitem()

# print(pop_items)
# print(type(pop_items))




# pop_item = user_info.pop('tuple')
# print(pop_item)
# print(type(pop_item))



# if user_info.get('names'):
#         print('yeah this is present')
# else:
#         print('sorry! not present')






