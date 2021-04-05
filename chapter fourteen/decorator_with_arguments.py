from functools import wraps

def only_allow_data_type(data_type):
    def decorator_function(anyfunc):
        @wraps(anyfunc)
        def wrapper(*args,**kargs):
            if all(type(arg)== data_type for arg in args):
                return anyfunc(*args,**kargs)
            return 'Envalid arguments'
        return wrapper
    return decorator_function

@only_allow_data_type(str)
def string_join(*args):
    string = ''
    for str in args:
        string += str
    return string

print(string_join('Mostafiz ','Rahman ','limon'))



