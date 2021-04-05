
# you can generate list by using list function and range method
#


# number = list(range(1,20,2))
#
# print(number)


# number = list(range(0,100,2))
# print(number)

# number = list(range(1,11))
# print(number.pop())    # pop method removes and return also the same value that should be remove
#
# print(number)

number = [1,2,3,4,5,6]

# def negative_list(l):
#     negative = []
#
#     for i in l:
#         negative.append(-i)
#
#     return negative
#
# print(negative_list(number))







# find the negative value of a list

number = list(range(1,11))
print(number)

def negative_number(x):
    another_number = []
    for i in x:
        another_number.append(-i)
    return another_number
print(negative_number(number))





