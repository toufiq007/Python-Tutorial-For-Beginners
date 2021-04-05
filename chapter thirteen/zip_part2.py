
l1= [1,2,3,4,5,6]
l2 = [10,20,30,40,50,60]



# find the max number of those list coupe item and store them into a new list


def find_max(l1,l2):
    new_array = []
    for pair in zip(l1,l2):
        new_array.append(max(pair))

    return new_array

print(find_max(l1,l2))





# find the smallest numbers and stored them into a new list

# another_list = []

# for pair in zip(l1,l2):
#     another_list.append(min(pair))

# print(another_list)







# l = zip(l1,l2)
# # print(list(l))
# print(dict(l))

# you have a list like 
# [(1,2),(3,4),(5,6)]
couple =  [(1,2),(3,4),(5,6)]

# you should convert this tuple into different list

l1,l2 = zip(*couple)

print(l1)
print(l2)





# l1,l2 = zip(*couple)

# print(l1)
# print(l2)


# zip_item = tuple(zip(l1,l2))

# print(zip_item)

# unpack_file,file = zip(*zip_item)
# print(unpack_file)
# print(file)













# new_list = []

# for pair in zip(l1,l2):
#     new_list.append(max(pair))

# print(new_list)










