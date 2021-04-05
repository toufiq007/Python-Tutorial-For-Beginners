

names = ['abc','def','ghi']





# make the reverse in every list item 

def reverse_list(x):

    reverse_item = []
    for i in range(len(names)):
        pop_items = names.pop()
        reverse_item.append(pop_items)

    return reverse_item

print(reverse_list(names))




words = ['abc','def','ghi']


def reverse_words(x):
    reverse_word_list = []

    for i in x:
        reverse_word_list.append(i[-1::-1])
    
    return reverse_word_list

# print(reverse_words(words))









# makes the reverse in every each item of the list
# def reverse_elements(x):
#     reverse = []
#     for i in x:
#         reverse.append(i[-1::-1])
#     return reverse

# print(reverse_elements(words))


































