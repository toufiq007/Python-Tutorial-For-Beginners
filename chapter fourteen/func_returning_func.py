# function returing function

# def outer_func(m):
#     def inner_func():
#         print(f'{m} inner function')
#     return inner_func

# func = outer_func('hello i am ')

# func()


# def outer_func():
#     def inner_func():
#         print('i am inner function')
#     return inner_func


# inner_func = outer_func()

# inner_func()


def outer_func(msg):
    def inner_func():
        print(f' {msg}.hello this is inner function')
    return inner_func

func = outer_func('first print this line and after then print the second function line')
func()


