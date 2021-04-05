
# dry ==> Don't repeat yourself

import random

# traditional way


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



# more simple way

winning_number = random.randint(1,100)
guess = 1
number = int(input('Enter a number between 1-100: '))
game_over = False

while not game_over:
    if winning_number == number:
        print(f' Congracts you win! by {guess} times')
        game_over = True

    else:
        if winning_number > number:
            print('too low')
        else:
            print('too high')

        guess += 1
        number = int(input('Again guess a number between 1-100: '))













