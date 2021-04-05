

# by using type function you can check what types of datatype is it 
# type method related problems


# check how many boolean value in a list

bool_list = [True,False,True,False]

# def bool_func(x):
#     counter = 0
#     for i in x:
#         if type(i) == bool:
#             counter +=1
#     return counter
# print(bool_func(bool_list))




# check how many list in your main list
# mixed = [1,2,3,4,[5,6,7],[9,7,10],[9,7,10]]
# def sublist_counter(x):
#     count = 0
#     for i in x:
#         if type(i) == list:
#             count += 1
#     return count

# print(sublist_counter(mixed))
    




# check how many string is in a list
total_words = ['banana','mango','apple']

# def all_words(x):
#     counter = 0
#     for i in x:
#         if type(i) == str:
#             counter +=1
#     return counter
# print(all_words(total_words))






# you can check any kind of data structure by using type function

mixed = [True,'Mosafiz',['apple','pear'],False,20,21,['rose','flower'],'limon']

def find_data_type(x):
    counter = 0
    for i in x:
        if type(i) == list:
            counter +=1
    return counter
print(find_data_type(mixed))






































