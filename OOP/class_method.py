# class method and class method as a constructor


class Person:
    count_inst = 0
    def __init__(self,first_name,last_name,age):
        Person.count_inst +=1

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)
   

    @classmethod
    def count_instance(cls):
        return f'you have created {cls.count_inst} instances of {cls.__name__} class '

    def full_name(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name
    

p1 = Person('Mostafiz','limon',20)
p2 = Person('toufiq','limon',21)

# print(p1.full_name())
# print(Person.count_instance())

p3 = Person.from_string('Tamim,hassan,23')
print(p3.full_name())
print(p3.age)
        


























