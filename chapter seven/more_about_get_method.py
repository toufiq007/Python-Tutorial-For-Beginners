

# in a dictionary at a same time you can't store same key name another time if you do so then second one overite the first value


# when the get method didn't fint what are checking then it show the output None..None is default value you can change the None in your own way by the passing 2nd arguement in the get method


personal_info ={
    'name' : 'Mostafiz limon',
    'age' : 30,
    'hobby' : 'programming',
    'lang' : ['javaScript','python','html','css'],
    'fav_songs':['you are not one','shape of you'],
    'age' : 20

}


# print(personal_info.get('fav_songs'))
# get_songs = personal_info.get('age')

# print(type(get_songs))

# print(personal_info.get('fav','not found!'))

print(personal_info)
print(personal_info.get('fav','not_found!'))










