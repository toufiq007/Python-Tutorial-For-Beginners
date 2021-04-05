
# exerise
# first collect user_name and age from the users
#



user_name,age = input('enter your name and age :').split(',')

age = int(age)

# first try

# if user_name[0] == user_name['a','A'] and age >=10:
#     print('you can watch this movie')
#
# else:
#     print('sorry! you can\'t watch this movie')



# success ways

if (user_name[0] == 'a' or user_name[0] == 'A') and age >=10:
    print('congrats!!you can watch this movies')

else:
    print('sorry!! you can\'t watch this movie.')






# user_name = user_name[0]
# print(f'the first letter of username is = {user_name} ')

