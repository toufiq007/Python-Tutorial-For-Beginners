
# local variable only works in the local scope
# global variable works in local scope also but you must declare it to gobal variable


# x = 20
#
# def function():
#     global x
#     x = 10
#     return x

# print(x)
# print(function())
# print(x)


name = 'toufiq limon'   # global variable or global scope
def newfunction():
    global name
    name = 'mostafiz limon'     # local variable or local scope
    return name


print(name)
print(newfunction())
print(name)







