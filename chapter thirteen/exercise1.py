


# define a function take any no of list containg with numbers
# [1,2,3],[4,5,6],[7,8,9]
# return avarage
# (1+4+7/3),(2+5+8/3),(3+6+9/3)

# try to make this with lambda expression

# l1 = [1,2,3]
# l2 = [4,5,6]
# l3 = [7,8,9]


l1 = [11,14,17]
l2 = [12,15,18]
l3 = [13,16,19]
l4 = [14,17,20]
l5 = [15,18,21]

(11,12,13,14,15)


# one way


def avarage_finder(*args):
    return [sum(pair)/len(pair) for pair in zip(*args)]

print(avarage_finder(l1,l2,l3,l4,l5))


avarage_finder = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(avarage_finder(l1,l2,l3,l4,l5))

# def avarage_finder(*args):
#     avarage_list = []
#     for pair in zip(*args):
#         avarage_list.append(sum(pair)/len(pair))
#     return avarage_list

# print(avarage_finder(l1,l2,l3,l4,l5))



# second way

# def avrg_finder(*args):
#     return [sum(pair)/len(pair) for pair in zip(*args)]


# print(avrg_finder(l1,l2,l3,l4,l5))




# third way

# find_avarage = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]

# print(find_avarage(l1,l2,l3,l4,l5))






