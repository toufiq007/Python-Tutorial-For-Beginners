
# do sum some of the numbers by using while loop

# find the sum of 1-100 digits by using while loop

# 0 to nth digits numbers sum is = n*(n+1)/2

# i = 0;
# sum = 0;
#
# while i<100:
#     i= i+1  # you can write also i += 1
#     sum = sum + i # you can write also sum += i
#     # print(f'Sum of the total number is = {sum}')


# print(f'sum of the total digits is = {sum}')





# problem number 1

# sum = 0
# number = int(input('enter your number: '))
#
# for i in range(0,number):
#     sum+=i
#
# print(f'sum of the {number} is = {sum}')
#






# problem number 2

# name = input('enter your name: ')
# i = 0
# total_str = ''
#
# while i< len(name):
#     if name[i] not in total_str:
#         total_str += name[i]
#         print(f'{name[i]} : {name.count(name[i])}')
#
#     i+=1



# problem number 3

# number = input('enter a number: ')
# total_num = 0
# for i in range(0,len(number)):
#     total_num+= int(number[i])
#
# print(f'total is = {total_num}')


# number = input('enter a number: ')
# i = 0
# total_num = 0
#
# while i < len(number):
#     total_num += int(number[i])
#     i+=1
# print(f'sum of the total numbe is = {total_num}')





# practice problem 4

# name = input('Enter your name: ')
# str = ''
#
# for i in  range(len(name)):
#     if name[i] not in str:
#         str+= name[i]
#
#         print(f'{name[i]} : {name.count(name[i])}')
#


#
# name = input('Enter your name: ')
# string_char = ''
#
# for i in range(0,len(name)):
#     if name[i] not in string_char:
#         string_char += name[i]
#         print(f'{name[i]} : {name.count(name[i])}')


# name = input('Enter your name: ')
# str = ''
# i=0
#
# while i<len(name):
#     if name[i] not in str:
#         str+= name[i]
#         print(f'{name[i]} : {name.count(name[i])}')
#     i+=1
#







import random

# winning_number = random.randint(1,100)
# guess_number = int(input('Please enter a number: '))
#
# i = 0
#
# while i < str(len(winning_number)):
#     if guess_number == winning_number:
#         print('yeah you win')
#
#     else:
#         if guess_number > winning_number:
#             print('too high')
#             again_guess = int(input('Again guess:'))
#             print(again_guess)
#
#         else:
#             print('too low')
#             another_guess = int(input('anothter guess'))
#             print(another_guess)
#



# winning_number = random.randint(1,100)
# guess = 1
# number = int(input('guess a number: '))
# game_over = False
#
# while not game_over:
#     if winning_number== number:
#         print(f'you win and you guess this number in {guess} times ')
#         game_over = True
#
#     else:
#         if winning_number > number:
#             print('too low')
#             guess += 1
#             number = int(input('guess again: '))
#
#         else:
#             print('too high')
#             guess += 1
#             number = int(input('guess again: '))
#





# modify the guessing game to add more fun

#
# winning_number = random.randint(1,100)
# guess = 1
# number = int(input('Enter a number between 1-100: '))
# game_over = False
#
# while not game_over:
#     if winning_number== number:
#         print(f'Congracts you win by {guess} times')
#         game_over = True
#
#     else:
#         if winning_number > number:
#             print(f'too low')
#             number = int(input('again give a number: '))
#             guess += 1
#
#         else:
#             print(f'too high')
#             number= int(input('again give a number: '))
#             guess +=1
#




wining_number = random.randint(1,100)
number = int(input('Enter your number between 1-100: '))
guess = 1
game_over = False

while not game_over:
    if wining_number == number:
        print(f' Congracts you win!! you win this game by {guess} times')
        game_over = True

    else:
        if wining_number > number:
            print(f'too low')

        else:
            print(f'Too high')

        guess += 1
        number = int(input(f'please enter again to win: '))


























