
# list comprehension

# print a list to square number of 1-10

# traditional way


num = list(range(1,11))

num_list = [i for i in range(1,11)]
print(num)

# def square_number(x):
#     square_list = []
#     for i in x:
#         square_list.append(i**2)
#     return square_list

# print(square_number(num))

square_list = []
for i in range(1,11):
    square_list.append(i**2)
# print(square_list)
# list comprehension way

square_list = [i**2 for i in range(1,11)]
print(square_list)





# square_list2 = [i**2 for i in range(1,11)]
# print(square_list2)



negative_number = [-i for i in range(1,11)]
# print(negative_number)

negative_number = [-i for i in range(1,11)]
print(negative_number)


negative_number = []
for i in range(1,11):
    negative_number.append(-i)
# print(negative_number)



names = ['limon','Mostafiz','toufiq']
new_list = []

# new_list_two = [i for i in names]
# print(new_list_two)

for i in names:
    new_list.append(i[0])
# print(new_list)


# another_list = [i[0] for i in names ]
# print(another_list)




