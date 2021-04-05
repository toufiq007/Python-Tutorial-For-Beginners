# you have to have a complete understanding of functions
# first class fucntions / closures
# then finally we will learn to decorators


def square(x):
    return x**2

s = square



# s = square  # it means square function is assign in s so s and square function is same things

print(s(7))

print(s.__name__)
print(square.__name__)

print(s)
print(square)






