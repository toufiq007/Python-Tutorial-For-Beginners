

# number_one = int(input('Enter first number: '))
# number_two = int(input('Enter second number: '))
#
# def greater_smallar(a,b):
#     if a>b:
#         return 'a is greater than b'
#     return  'b is greater than a'


# print(greater_smallar(number_one,number_two))

# greater = greater_smallar(number_one,number_two)
# print(f'{greater} is greater')






# problem two
# find the largest number of three number

def lastest_number(a,b,c):
    if a>b and b>c:
        return 'a is greater than b and c'
    elif b>a and b>c:
        return 'b is greater than a and c'
    else:
        return 'c is greater than a and b'

num_1= int(input('first number: '))
num_2= int(input('second number: '))
num_3= int(input('third number: '))
print(lastest_number(num_1,num_2,num_3))









