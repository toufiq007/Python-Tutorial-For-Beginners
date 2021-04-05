
# kwargs --> keyword arguments
# **kwargs --> double star operator

# no matter what is you give the argument in keyword arguments kwargs trasform it to a dictionary

# kwargs as a paratemter

# def func(**kwargs):
#     # print(kwargs)
#     # print(type(kwargs))
#     for k, v in kwargs.items():
#         print(f' {k} : {v} ')

# func(first_name= 'Mostafiz',last_name = 'limon')



# def func(**kwargs):
#     for k, v in kwargs.items():
#         print(f' {k} : {v} ')

# dic = {
#     'first_name' : 'Mostafiz',
#     'last_name' : 'toufiq'

# }
# func(**dic)


def myfunc(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k, v in kwargs.items():
        print(f'{k}: {v} ')


dic = dict(name= 'mostafiz',age= 20,hobby= 'programming')

myfunc(**dic)




