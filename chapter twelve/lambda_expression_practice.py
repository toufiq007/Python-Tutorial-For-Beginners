
# declare function in one way

def is_even(a):
    if a%2==0:
        return True
    return False


print(is_even(7))

# is_odd = lambda a: a%2!=0
# print(is_odd(10))




# declare function in another way

# def is_even(a):
#     return a%2==0
# print(is_even(4))



# declare function in another way

# is_even = lambda a : a%2==0
# print(is_even(10))


# is_odd = lambda a : a%2 !=0
# print(is_odd(9))




# find last_char in general way

# def last_char(x):
#     return x[-1].upper()
# print(last_char('limon'))



def last_char(x):
    return x[-1].upper()
print(last_char('mostafiz'))





# find last_char with lambda expression

# last_char = lambda x : x[-1].upper()
# print(last_char('limon'))

last_char = lambda a : a[-1].upper()
print(last_char('mostafiz'))



# find the length of a string

# def str_len(x):
#     if len(x) > 5:
#         return 'the length is greater than 5'
#     return 'the lenght is smaller than 5'
# print(str_len('limondd'))



# str_len = lambda a : True if len(a)>5 else False
# print(str_len('Mostafiz'))


# str_len = lambda a : len(a) > 5
# print(str_len('most'))


def str_length(x):
    if len(x)> 5:
        return 'the length of the string is greater than 5'
    return 'the length of the string is less than 5'

print(str_length('mostafiz'))



str_length = lambda s: len(s) > 5
print(str_length('limon'))

