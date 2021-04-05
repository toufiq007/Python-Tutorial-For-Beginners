

import random

number = random.randint(0,20)
guess_number = int(input('please guess a valid number between (0-20) '))
print(f'the correct number was {number}')


if number == guess_number:
    print('yeap! congratulations you win !!')

# elif number < guess_number:
#     print('sorry! this is not so..you pick too high number')
#
# elif number > guess_number:
#     print('sorry! this is not so..you pick too low number')

else: # this is called nested if else statement

    if number < guess_number:
        print('sorry! too high')

    else:
        print('sorry! too low')





