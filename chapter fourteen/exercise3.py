from functools import wraps


# def calculate_total(any_func):
#     @wraps(any_func)
#     def wrapper_function(*args,**kargs):
#         if all(type(arg) == int for arg in args):
#             return any_func(*args,**kargs)
#         else:
#             return 'wrong information'

#         # data_types = []
#         # for arg in args:
#         #     data_types.append(type(arg) == int)
#         # if all(data_types):
#         #     return any_func(*args,**kargs)
#         # else:
#         #     return 'you pass the wrong items'
#     return wrapper_function
  


def check_type(any_func):
    @wraps(any_func)
    def wrapper_function(*args,**kargs):
        if all(type(arg)==int for arg in args):
            return any_func(*args,**kargs)
        else:
            return 'please give the right value'
        # data_type=[]
        # for arg in args:
        #     data_type.append(type(arg)==int)
        # if all(data_type):
        #     return any_func(*args,**kargs)
        # else:
        #     return 'please enter right value'
    return wrapper_function




@check_type
def total_add(*args):
    total = 0
    for i in args:
        total +=i
    return total


print(total_add(1,2,3,4,5))





