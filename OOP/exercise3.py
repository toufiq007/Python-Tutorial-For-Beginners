
class Person:

    count_instancs = 0

    def __init__(self,name,age):
        Person.count_instancs+=1
        self.name = name
        self.age = age
        
  
p1 = Person('mostafiz',20)
p2 = Person('toufiq',21)

print(Person.count_instancs)








