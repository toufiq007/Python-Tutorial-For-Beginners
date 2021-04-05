
# Encapsulation
# Abstraction
# Some Exceoptional Naming Convention
# Name Mangling


class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.__price = price

    
    def make_a_call(self,phone_number):
        print(f'Calling {phone_number} ')
    

    def full_name(self):
        return f'Your phone is {self.brand} {self.model} '


phone1 = Phone('nokia',1100,1500)

print(phone1.__dict__)

print(phone1._Phone__price)

phone1._Phone__price = 1200
print(phone1._Phone__price)

# _price # convention of private method
# __name__ # dunder mothod or magic method

        












