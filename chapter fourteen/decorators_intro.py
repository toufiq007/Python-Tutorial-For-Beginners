# Decorators - enhance the functionally of others function
# first declare a decorator function pass the input any kinds of functions 
# sintactive sugar ==> first give @ and then give the decorator name what should you create
# like ==> @decorator_function



# def decorator_function(any_function):
#     def wrapper_function():
#         print('hello decorator function inhance the main functions power')
#         any_function()
#     return wrapper_function


# @decorator_function     # it is the sortcut to use decorator function without make any variable and so



def decorator_function(any_function):
    def wrapper_function():
        print('this is decorator function')
        any_function()
    return wrapper_function



@decorator_function
def func1():
    print('this is function one')


@decorator_function
def func2():
    print('this is function two')


func1()

# func2()









