

# name = 'civic'
#
# final_name_one = name[-1::-1]
#
# if name == final_name_one:
#     print('this is palindrome')
#
# else:
#     print('this is not palindrome')


name = input('Enter a name to know is it palindrome: ')
# name = 'madam'


# conventional way

# def is_palindrome(name):
#     reverse_name = name[-1::-1]
#     if name== reverse_name:
#         return 'the name is a palindrome'
#     else:
#         return 'the name is a not palindrome'
#
# print(is_palindrome(name))



# another way

# def is_palindrome(name):
#     if name == name[-1::-1]:
#         return 'this is a palindrome'
#     return 'this is not a palindrome'
# print(is_palindrome(name))




# another sortest way

def is_palindrome(name):
    return name == name[-1::-1]

print(is_palindrome(name))















