
# def greater_smallar(a,b):
#     if a>b:
#         return 'a is greater than b'
#     return  'b is greater than a'
#
# # print(greater_smallar(10,20))
#
#
# def new_greatest(a,b,c):
#     bigger = greater_smallar(a,b)
#     return greater_smallar(bigger,c)
#
#
# print(new_greatest(10,20,30))



# main function define in another function

def greater(a,b):
    if a > b:
        return a
    else:
        return b

def greatest_number(x,y,z):
    bigger = greater(x,y)
    return greater(bigger,z)
print(greatest_number(10,20,30))


