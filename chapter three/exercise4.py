

# easy but not right way

# user_number = input('give a four digit number: ')
# total_number = int(user_number[0]) + int(user_number[1]) + int(user_number[2]) + int(user_number[3])
#
# print(f'total_number is = {total_number} ')
# print(user_number[0])



# best ways
# digit = input('please enter a large digit number: ')
#
# total_number = 0;
# i = 0
#
# while i < len(digit):
#     total_number+= int(digit[i]);
#     i+=1
#
# print(f'total sum of the digit is = {total_number}')





number = input('Enter a number: ')
sum = 0
i = 0

while i < len(number):
    sum += int(number[i])
    i+= 1
print(f'sum of the {number} is ={sum}')

















