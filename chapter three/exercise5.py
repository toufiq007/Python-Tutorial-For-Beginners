
# get a name form the user and check every character how many times are in the string

# hints
# counter= name.count(name[i])
# print(f'{name[i]} : {counter}')

# name = input('enter your name: ')
#
# i = 0
# tem_var = ''
# while i < len(name):
#
#     if name[i] not in tem_var:
#         tem_var+= name[i]
#         print(f'{name[i]} : {name.count(name[i])}')
#
#     i+=1

#
# i = 0
# total_letter = '';
#
# while i < len(name):
#     if name[i] not in total_letter:
#         total_letter+= name[i]
#         print(f'{name[i]} : {name.count(name[i])}')
#
#     i+=1
#

#
# while True:
#     print('hello bangladesh')





# name = input('Enter a name: ')
# temp_letter = ''
# i =0

# while i < len(name):
#     if name[i] not in temp_letter:
#         temp_letter += name[i]
#         print(f'{name[i]} : {name.count(name[i])}')

#     i+=1









# word counter by using for loop

name = 'toufffiqqq'
temp_str = ''

for i in range(len(name)):
    if name[i] not in temp_str:
        temp_str += name[i]
        print(f' {name[i]} : {name.count(name[i])}')
