
# function with all parameters
# very important to understand


# PADK 

# parameter --> normal parameter
# **args -->  *argument
# default parameter --> which is set form before
# **kwargs --> double **argument


# def func(name,*args,last_name='unknown',**kwargs):
#     print(name)
#     print(args)
#     print(last_name)
#     print(kwargs)

# func('Mostafiz','limon','rahman limon',hello='limon')




# def func2(name,last_name= 'unknown'):
#     print(name)
#     print(last_name)

# func2('limon','rahman limon')







# def func(name,*args):
#     print(name)
#     print(args)
#     print(type(args))

#     new_name_list = []

#     for i in args:
#         new_name_list.append(i)
    
#     return new_name_list

# print(func('limon',1,2,3,4,5,6))





# def func(name,**kwargs):
#     # print(name)
#     # print(kwargs)

#     print(type(kwargs))


#     for i, j in kwargs.items():
#         return (f' {i} : {j} ')

# print(func('mostafiz',first_name = 'Mostafiz limon'))









