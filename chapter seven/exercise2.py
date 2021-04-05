
user = {}
# name,age,fav_movie,fav_songs = input('Enter your name,age,fav_movie,fav_songs: ').split(',')


name = input('what is your name? ')
age = input('what is your age? ')
fav_movies = input('your favourtie movies are separated by comma ').split(',')
fav_songs = input('your favourite songs are separated by comma ').split(',')


user['name'] = name
user['age'] = age
user['fav_movies'] =fav_movies
user['fav_songs'] =fav_songs


# print(user)


# for i in user:
#     print(f' {i} : {user[i]} ')

for key, value in user.items():
    print(f' {key} : {value} ')










# def user_info(n,a,m,s):
#     user_dict = {}
#     for i in n:
#         user_dict[i] = 'limon'
#     return user_dict
# print(user_info(name,age,fav_movie,fav_songs)) 






