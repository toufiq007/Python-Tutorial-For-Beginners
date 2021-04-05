
from functools import wraps

def print_function_data(any_func):
    @wraps(any_func)
    def wrapper_function(*args,**kargs):
        print(f'you are calling {any_func.__name__} function')
        print(f' {any_func.__doc__} ')
        return any_func(*args,**kargs)
    
    return wrapper_function


@print_function_data
def add(x,y):
    ''' this function two arguments of numbers and return their sum '''
    return x+y

print(add(10,15))






