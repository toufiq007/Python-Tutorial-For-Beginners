
def even_num(x):
    for i in range(2,x+1,2):
        yield(i)
       


for i in even_num(10):
    print(i)

for j in even_num(10):
    print(j)







