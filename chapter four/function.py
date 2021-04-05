
# write your first functions in python
# function is very essectial for coding
# when you make a function in python you can use anywhere in your project and where you want
# just declare the function with arguements and that's all


# syntex:
# 1: step one: first write def keyword
# 2: step_two: second write a valid function name with arguements
# 3: step_three: third_write a function body means what things should you want to do


def add_two_number(x,y):
    return x + y

# total = add_two_number(10,20)
# print(f'total = {total}')


# print(add_two_number(10,20))

# x,y = input('Enter two number separating by comma: ').split(',')
# x = int(x)
# y = int(y)




# exmple one

# main_function

def sum(x,y):
    # return x + ' ' + y  # for string
    return x + y  # for numbers like integers and floating number



# total = sum(first_name,last_name)
# print(f'sum is = {total}')



# first_name = input('Enter your first_name: ')
# last_name = input('Enter your last_name: ')
#
#
# print(sum(first_name,last_name))



number_one = int(input('first number:'))
number_two = int(input('second  number:'))

print(sum(number_one,number_two))
