

# join and split method in python


# split() method is used to convert string to list
# split() == string ==> list

# name = 'mostafiz'.split(' ')
# age = '20'.split(' ')
#
#
# print(name,age)
#
#
# user_information = name.append(age)
# print(user_information)


user_info = 'mostafiz,20'.split(',')

# user_info = ['mostafiz',20]
bio = ['limon,30']

# user_info.append(bio)
# user_info.extend(bio)
# print(user_info)


# print(user_info)
# print(bio)
#
# user_info.append(bio)
# print(user_info)
# user_info.extend(bio)
# print(user_info)
#
#
# user_info.reverse()
# print(user_info)
#






# join() method converts list to string

# join() == list ==> string

user_info = ['toufiq','20','madaripur']

convert_string = '\n'.join(user_info)

print(convert_string)








