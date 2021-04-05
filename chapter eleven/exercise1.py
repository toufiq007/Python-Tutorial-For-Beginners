



# this way

# def power_function(nums,*args):
#     return_list = []

#     if args:
#         for i in args:
#             return_list.append(i**nums)
#         return return_list
#     else:
#         return ('give a valid numbers')
        
# nums = [1,2,3,4,5]

# print(power_function(3,))




def power_func(nums,*args):
    if args:
        return [i**nums for i in args]
    else:
        return 'you donot give a number_list'

nums = [1,2,3,4,5]

print(power_func(3,))




# how to check your list is empty or not

l = []

if len(l) > 0:
    print('list is not empty')
else:
    print('list is empty')

















# def power_function(num,*args):
#     if args:
#         return [i**num for i in args]
#     else:
#         return "you don\'nt give any arguments"

# print(power_function(3,*[1,2,3,4,5]))



def power_up(num,*args):
    argument_list = []

    if args:
        for i in args:
            argument_list.append(i**num)
        return argument_list
        
    else:
        return 'you did\'nt give any argument'
# number_list = [1,2,3,4,5,6,7,8,9]
# print(power_up(3,*number_list))





# another way

# def power_func(x,*args):
#     if args:
#         return [i**x for i in args]
#     else:
#         return 'you didn\'t pass any arguemnts'
    
# nums = [1,2,3,4,5,6]
# print(power_func(3,*nums))


