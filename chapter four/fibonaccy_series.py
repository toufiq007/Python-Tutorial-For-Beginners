
# fibonacci series


def febonacci_seq(n):
    a = 0
    b = 1

    for i in range(2,n):
        c = a+b
        a = b
        b = c

        print(b)

febonacci_seq(10)