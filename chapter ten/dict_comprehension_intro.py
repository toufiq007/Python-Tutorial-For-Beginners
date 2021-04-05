

user_info ={
    'name' : 'limon',
    'age' : 20,
    'hobby' : 'programming',
    'lang' : ['javascript','python']
}


# print(user_info)
# print(type(user_info))

# for key, value in user_info.items():
#     print(f' {key} and {value}  ')


# square = {i: i**2 for i in range(1,11) }
# print(square)

# when you use f string in dictionary in dict comprehension then it's return a set where store values



# square = {f'square of {i} : {i**2} ' for i in range(1,11)}
# print(square)
# print(type(square))
# square = {f'square of {i}':i**2 for i in range(1,11) }

# print(square)
# print(type(square))




square = {f' {i}' : i**2 for i in range(1,11)}
# print(square)
# print(type(square))


# for key, value in square.items():
    # print(f'key is {key} and value is {value} ')
    # print(f' {key} : {value} ')

# print(type(square))









# word counter by dictionary comprehension

name = 'limon'

name = {char:name.count(char) for char in name}

print(name)

for key,value in name.items():
    print(f' {key} : {value} ')









