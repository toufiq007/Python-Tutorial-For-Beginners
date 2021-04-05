# make flexible functions
# when you need to pass more arguemnts then you must use *args --> star arguments 


# *operator
# *args


# def total(*args):
#     print(args)
#     print(type(args))

# total(1,2,3,4,5,6,7,8,9)


# def total_number(*args):
#     sum = 0
#     for i in args:
#         sum+=i
#     return (f'total is = {sum} ')

# print(total_number(1,2,3,4,5,6,7,8,9))



# def myFun(arg1, *argv): 
#     print ("First argument :", arg1) 
#     for arg in argv: 
#         print(f"Next argument through *argv : {arg} ") 
  
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')




def myfunc(x,*args):
    print(f'first argument : {x} ')

    for i in args:
        print(f'second arguements through args : {i} ')

myfunc('hello','mostafiz-limon','how','are','you?')