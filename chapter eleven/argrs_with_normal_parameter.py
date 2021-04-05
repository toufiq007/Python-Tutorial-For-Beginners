
# *args with normal parameters


# def multipy(*args):
#     multipy_nums = 1
    
#     for i in args:
#         multipy_nums *= i
#     return multipy_nums

# print(multipy(1,2,3,4,5,6))



# def total(num,num1,*arg):
#     print(num)
#     print(num1)
#     print(arg)
#     total_sum = 0
#     for i in arg:
#         total_sum+= i
#     return total_sum
# print(total(1,2,3,4,5))




# def another_name(x,y,*args):
#     print(x)
#     print(y)
#     print(type(x))
#     print(type(y))
#     print(args)
#     print(type(args))


# print(another_name('limon','toufiq','Mostafizur','Rahman','Limon'))


# when you use star arguement in first with normal arguemnt then you got error because *args keep all the arguemnts that you give  

# you must use *args in the order of last to your normal arguemnts


def number(x,*args):
    print(args)
    print(x)

    sum = 0
    for i in args:
        sum+=i
    return sum


print(number(1,2,3,4,5,6))





