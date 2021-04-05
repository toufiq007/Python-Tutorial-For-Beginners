

names= ['limon','toufiq','mostafiz']
# another_name = input('please e name to find: ')




def find_name(names,target_name):
    for name in names:
        if name == target_name:
            return names.index(name)
    return -1

print(find_name(names,'mostafiz'))





# using general functions

# pos = 0

# def find_pos(names,target_name):
#     for name in names:
#         if name == target_name:
#             return names.index(name)
#             pos+=1
#     return -1

# print(find_pos(names,'mostafiz'))



# pos = 0

# def find_pos(names,target_name):
#     for name in names:
#         if name == target_name:
#             return names.index(name)
#     return -1

# print(find_pos(names,'mostafiz'))




# def find_pos(names,target_name):
#     for pos, name in enumerate(names):
#         if name== target_name:
#             return pos
#     return -1

# print(find_pos(names,'toufiq'))  





# using enumerate functions

# def find_pos(names,target_name):
#     for pos, name in enumerate(names):
#         if name== target_name:
#             return pos
#     return -1


# print(find_pos(names,'limon'))







