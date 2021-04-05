
# show ticket pricing

age = input('please enter your age to know the ticket price: ')
age = int(age);



# one way

# if age ==0 and age <=3:
#     print('your ticket is free')
#
# elif age >=4 and age <=10:
#     print('your ticket price is 150 tk')
#
# elif age>=11 and age<=60:
#     print('your ticket price is 250 tk')
#
# else:
#     print('your ticket price in 200 tk')



# another way

if 0<=age<=4:
    print('your ticket is free')

elif 4<=age<=10:
    print('your ticket is 150 tk')

elif 11<=age<=60:
    print('your ticket is 250 tk')

else:
    print('your ticket is 200 tk')

