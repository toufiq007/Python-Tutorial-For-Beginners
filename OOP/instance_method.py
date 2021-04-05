
# instance method

class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def full_name(self):
        full_name = self.first_name+ ' ' +  self.last_name
        return full_name

    def is_avobe(self):
        return self.age > 18


p1 = Person('Mostafiz','Limon',11)
p2 = Person('Tamim','Hassan',21)

print(p1.first_name)
print(p1.last_name)
print(p1.full_name())
print(p1.is_avobe())

# print(p2.full_name())




