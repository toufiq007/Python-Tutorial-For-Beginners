# decorator function part two


# main way to write decorator function
from functools import wraps




def decorator_function(anyfunc):
    @wraps(anyfunc)
    def wrapper_function(*args,**kargs):
        ''' this is wrapper function '''
        print('this is awesome function')
        return anyfunc(*args,**kargs)
    
    return wrapper_function

# @decorator_function
# def func():
#     print('hello this is new function')

# func()


# @decorator_function
# def add(x):
#     print(f'this is awesome function with arguemnts {x} ')


# add(5)



@decorator_function
def add(x,y):
    ''' this is add function '''
    return x+y

print(add(10,10))


print(add.__doc__)
print(add.__name__)





