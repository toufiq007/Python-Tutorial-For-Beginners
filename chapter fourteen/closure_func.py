# function returing function(closures) practice

# closures is function returning function from another fucntion



# def to_power(x):
#     def calc_power(n):
#         return n**x
#     return calc_power


# power_func = to_power(5)
# print(power_func(2))



def to_power(x):
    def base_number(n):
        return n**x
    return base_number

power_off = to_power(4)
print(power_off(3))






