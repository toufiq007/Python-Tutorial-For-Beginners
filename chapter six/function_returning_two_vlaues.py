
# returing function with two values
# when you return two values in a function this fucntion can't return two values it returns one value with a tuple number



def func(x,y):
    # return (x+y),(x-y)
    add = x +y
    mul = x *y
    return add , mul
    

add,mul = func(3,2)

print(add)
print(mul)









