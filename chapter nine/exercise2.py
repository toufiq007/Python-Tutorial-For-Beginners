
# store a different list only numbers by using simple mode or list comprehension mode


input_list = [True,False,[1,2,3],'limon',(1,2,3,4),10.5,2.4,1,4,8,10]

output_list = []

# general mode or simple mode

for i in input_list:
    if type(i) ==int or type(i) ==float:
        output_list.append(str(i))
print(output_list)



# list comprehension mode

output_list = [str(i) for i in input_list if type(i) == int or type(i) == float]
print(output_list)








