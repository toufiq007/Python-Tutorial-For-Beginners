

number = list(range(1,11))
print(number)

# new_number = []


# for i in number:
#     if i%2==0:
#         new_number.append(i*2)
#     else:
#         new_number.append(-i)
# print(new_number)


# list comprehension with if else

new_number = [i*2 if(i%2==0) else(-i) for i in number]
print(new_number)














