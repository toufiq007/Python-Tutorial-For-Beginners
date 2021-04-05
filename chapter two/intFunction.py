
# int function in python
# when you can change a string_number to number then you can use int() function



#inportant notes
# str() => convert number to string like 4---> "4"
# int() => convert string to number like "4"--> 4
# float() => convert number to floating number '4'-->4.00

# you can add int with float but final answer shows in float


# method 1
# number1 = int(input('Please enter a new number'))
# number2 = int(input('please enter another number'))
# total_number = number1 + number2
# print(total_number)



# method 2
# number_one = input('give a number')
# number_two = input('give a another number')
# total = int(number_one) + int(number_two)
# print('total number is = ' + str(total))


number = input('enter your first number')
number_two = input('enter your second number')

modulas = int(number) % int(number_two)
print('total value is = ' + str(modulas))



