
# when you want to make a dictionary and give various keys same value defaultly then you should use formkeys..
# exmple below


# d = dict.fromkeys(['name','age','height'],'unknown')
# print(d)

# d = dict.fromkeys(['name','age','hobby','height'],['unknown','unknown'])
# print(d)


d = dict.fromkeys(['name','age','height','address'],'unknown')

print(d)


# get method (usefull)   --> better to find check the key if is it in dictionary or not

# when you give this kind of value that's should be ont in the dictionary then get method doesn't give the error it give you the output None ...it means thas't not in the dictionary


# d = {
#     'name' : 'Limon',
#     'age' : 20
# }


# get_name = d.get('age')
# print(get_name)
# print(type(get_name))


# if 'name' in d:
#     print('present')
# else:
#     print('not present')




# When you use get method with dictionary in if or else then if get find a valid key then it evaluated true and if scope will be executed   and  when get method did'nt find any valid key then it evaluated false and else scope will be executed


# first condition

# if d.get('name'):
#     print('present')
# else:
#     print('not present')

# second condition

# if d.get('names'):
#     print('present')
# else:
#     print('not_present')

# if none -----> False ,      else -----> True



personal_info ={
    'name' : 'limon',
    'age' : 20,
    'hobby' : 'programming'
}


# if 'name' in personal_info:
#     print('present')
# else:
#     print('not present')

# if personal_info.get('names'):
#     print('present')
# else:
#     print('not present')

# clear method
# you can clear your dictionary by using clear method
# d.clear()
# print(d)




# copy method
# you can copy your dictinary with another dictionary by using copy method

d1 = d.copy()

d1 = d  # it means two are same dictionary

# print(d1)
# print(d1.popitem())
# print(d)



