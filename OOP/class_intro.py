
# make your first class
# what is class
# how can we define it
# what is init method ==> like almost constructor
# what are attribute and instance variables
# how can create an object


class Person:
    def __init__(self,first_name,last_name,age):

        # instance variables
        print('hello constructor')
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    
p1 = Person('Mostafiz','limon',20)
p2 = Person('toufiq','Rahman',19)


print(p1.first_name)
print(p2.first_name)

        
















