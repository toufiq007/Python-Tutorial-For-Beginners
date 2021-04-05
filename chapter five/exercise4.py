

number = [1,2,3,4,5,6,7,8,9,10,11]
print(number)

def odd_even(x):
    odd =[]
    even = []

    for i in x:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return odd,even

print(odd_even(number))

















# def odd_even(x):
#     odd = []
#     even = []

#     for i in x:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
    
#     return odd , even
# print(odd_even(number))














#  for i in number:
#     odd = []
#     even = []

#     if i%2==0:
#         odd.append(i)
#         # print(odd)

#     else:
#         even.append(i)
#         # print(even)

#     odd.append(even)

#     print(odd)

