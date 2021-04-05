
# Args as arguements 


def multiply_nums(*args):
    print(args)
    print(type(args)) # [1,2,3,4,5]

    mutiply = 1
    for i in args:
        mutiply *= i
    return mutiply

# when you pass a list or tuple by arguemnts in your function then you must give * argument after give your list or tuple name

number = [1,2,3,4,5]
print(multiply_nums(*number)) # when you pass the * arguements then the items of the list will unpack.


    













