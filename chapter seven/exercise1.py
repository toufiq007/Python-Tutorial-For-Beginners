


# def cube_func(x):
#     cube_dic = dict()
#     for i in x:

#         num = i**3
#         number_dic = {
#             i : num
#         }
#         cube_dic.update(number_dic)
#     return cube_dic


# number = list(range(1,10))
# print(cube_func(number))











# make a function that function take a single number and convet it to cube number and returns it into a dictionary

# like {1:1, 2:8, 3:27}

# def cube_func(x):
#     cube_dict = dict()

#     for i in x:
#         cube_number = i**3
#         another_cube_dict = { i : cube_number }
#         cube_dict.update(another_cube_dict)
#     return cube_dict

# number = list(range(1,10))
# print(cube_func(number))



def cube_dict(x):
    cube_list = {}
    for i in x:
        cube_list[i] = i**3
    return cube_list

number = list(range(1,10))
print(cube_dict(number))






















# another way

# def cube_finder(x):
#     cubes = {}
#     for i in range(1,x+1):
#         cubes[i] = i**3
#     return cubes

# print(cube_finder(10))





