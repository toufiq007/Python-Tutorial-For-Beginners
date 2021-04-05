
names = ['limon','toufiq','salman']


# def capital_str(name):
#     new_name_list = []

#     for i in name:
#         # new_name = i[0].capitalize()
#         new_name_list.append(i[::-1].capitalize())
#     return new_name_list

# print(capital_str(names))


# def cappital_str(name):
#     name_list = []

#     for i in name:
#         name_list.append(i[::-1].upper())
#     return name_list

# print(cappital_str(names))





# make this by using list comprehension way

def captital_string(x,**kwargs):
    if kwargs.get('reverse_string'):
        return [i[::-1].upper() for i in x]
    else:
        return [i.title() for i in x]

print(captital_string(names,reverse_string=True))





# make this by using general way

def captital_str(name,**kwargs):
    reverse_str_list = []
    if kwargs.get('reverse_str'):
        for i in name:
            reverse_str_list.append(i[::-1].upper())
        return reverse_str_list
        
    else:
        return [i.upper() for i in name]

print(captital_str(names,reverse_str=True))











# def captital_str(name,**kwrags):
#     if kwrags.get('reverse_str')==True:
#         return [i[::-1].upper() for i in name]
#     else:
#         return [i.title() for i in name]

# print(captital_str(names,reverse_str=True))













# def funct(x,**kwargs):
#     if kwargs.get('reverse_str'):
#         return [name[::-1].upper() for name in x]
#     else:
#         return [name.upper() for name in x]

# print(funct(names,reverse_str=True))











# def funct(x,**kwargs):
#     if kwargs.get('reverse_str')==True:
#         return [i[::-1].upper() for i in x]
#     else:
#         return [i.upper() for i in x]




# print(funct(names,reverse_str= True))









