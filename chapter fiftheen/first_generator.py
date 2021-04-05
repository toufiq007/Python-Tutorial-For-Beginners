# create your first generator with generator functions

# 1) generator function
# 2) generator comprehension

import time


# without generator


t1 = time.time()
def number(x):
    for i in range(1,x+1):
        print(i)

number(10)

t2 = time.time()

print(t2-t1)





# with generator


t1 = time.time()

def numbers(x):
    for i in range(1,x+1):
        yield(i)

numbers1 = numbers(10)
for num in numbers1:
    print(num)
t2 = time.time()

print(t2-t1)


