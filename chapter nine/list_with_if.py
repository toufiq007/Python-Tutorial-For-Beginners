

number = list(range(1,11))

# print(number)


even_list = []

for i in number:
    if i%2==0:
        even_list.append(i)

# print(even_list)

even_nums = [i for i in number if i%2==0]
odd_nums = [i for i in number if i%2 != 0]
print(odd_nums)
print(even_list)






