
# filter function in python

# def is_even(x):
#     if x%2==0:
#         return 'number is even'
#     return 'number is odd'
    

# print(is_even(9))


number = [2,3,4,5,6,7,8,9,23,34,12,32,100]


# def filter_number(x):
#     odd_number = []
#     for i in x:
#         if i%2==0:
#             odd_number.append(i)
#     return odd_number
# print(filter_number(number))


def filter_number(x):
    return x%2==0


# flter= list(filter(filter_number,number))
# print(flter)


flter = filter(lambda x: x%2==0,number)


for i in flter:
    print(i)








