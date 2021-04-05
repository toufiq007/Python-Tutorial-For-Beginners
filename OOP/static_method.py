
# static method

class Person:

    def __init__(self,first_name,last_name,age):
       

        self.first_name = first_name
        self.last_name = last_name
        self.age = age



    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)
   
    @staticmethod
    def hello():
        print('hello static method called')


    def full_name(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name
    

p1 = Person('Mostafiz','limon',20)
p2 = Person('toufiq','limon',21)



p3 = Person.from_string('Tamim,hassan,23')
print(p3.full_name())
print(p3.age)

Person.hello()










