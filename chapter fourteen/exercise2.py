
from functools import wraps
import time



def calculate_time(any_func):
    
    @wraps(any_func)
    def wrapper_function(*args,**kargs):
        print(f'Execution time of {any_func.__name__} function ')
        t1 = time.time()        
        returned_value = any_func(*args,**kargs)
        t2 = time.time()
        total_time = t2 - t1
        print(f'this function took  {total_time} second  ')

        return returned_value
        
    return wrapper_function
    

@calculate_time
def func():
    for i in range(4):
        print('hello bangladesh')

func()








