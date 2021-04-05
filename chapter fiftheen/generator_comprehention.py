
# def generator_number(x):
#     for i in range(x+1):
#         if i%2==0:
#             yield(i)

# number = generator_number(10)
# for num in number:
#     print(num)


def list_comprehension(x):
    return (x**2 for x in range(x+1))

generator_object = list_comprehension(10)
# print(generator_object)

# for square in generator_object:
#     print(square)

print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))
print(next(generator_object))



