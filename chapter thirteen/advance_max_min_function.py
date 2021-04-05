
# advance max and min function in python



#exmple one
name = ['Mostaifz','limon','Toufiq']
# find_max = max(name,key= lambda items: len(items))

# print(find_max)

#exmple two
students_one ={
    'Mostafiz' : {'score':90,'age':20},
    'Toufiq' : {'score': 80,'age':21}
}

# print(max(students_one,key=lambda items: students_one[items]['age'] ))
    

# Exmple three

students_two = [
    {'name': 'Mostafiz','score' :90,'age': 20},
    {'name': 'Toufiq','score' :100,'age': 22},
    {'name': 'Limon','score' :80,'age': 21},
]

print(max(students_two,key=lambda items: items.get('age')).get('name'))






