
# dictionary comprehension with if else

# d = {i:i**2 for i in range(1,10)}
# print(d)



odd_even = {i:('even' if i%2==0 else 'odd') for i in range(1,11)}
print(odd_even)
# print(odd_even)


another_list = {-i**2 if i%2!=0 else i**2 for i in range(1,10)}

# print(another_list)
# ltr = dict(another_list)
# print(ltr)
# print(type(ltr))

# for i, j in ltr.items():
#     print(f'{i} : {j}  ')











