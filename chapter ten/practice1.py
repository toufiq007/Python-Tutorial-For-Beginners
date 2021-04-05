
# practice one

# number = list(range(1,11))

# print(number)

# another_number= []

# for i in range(len(number)):
#     pop_items = number.pop()
#     another_number.append(pop_items)
# print(another_number)





# practice two

# names = ['limon','salman','tamim']

# print(names)
# another_names = []
# for i in range(len(names)):
#     another_names.append(names.pop())
# print(another_names)




# practice three

# names = ['limon','rudro','atiqur']

# another_names= []

# for i in names:
#     another_names.append(i[::-1])
# print(another_names)




# practice 4

# name = 'limon'
# print(name)
# word_counter = {i:name.count(i) for i in name}

# print(word_counter)
# for key, value in word_counter.items():
#     print(f'{key} : {value}  ')



# practice 4 another way

# name = 'toufffiqqq'
# temp_str = ''

# for i in range(len(name)):
#     if name[i] not in temp_str:
#         temp_str += name[i]
#         print(f' {name[i]} : {name.count(name[i])} ')






# practice 5

# number_list = [i for i in range(1,11) if i%2==0]
# print(number_list)


# practice 5 another way

# number = list(range(1,11))
# number_list = []

# for i in number:
#     if i%2 ==0:
#         number_list.append(i)
# print(number_list)







# practice 6

# number_list = [i*2 if i%2==0 else (-i) for i in range(1,11)]
# print(number_list)



# practice 6 another way


number_list = []


for i in range(1,11):
    if i %2==0:
        number_list.append(i*2)
    else:
        number_list.append(-i)

print(number_list)












