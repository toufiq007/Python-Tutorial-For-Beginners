

class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self._price = max(price,0)
        # self.full_specs = f'your phone is {self.brand} {self.model} and price is {self._price} '
    
    @property
    def complete_specs(self):
        return f'your phone is {self.brand} {self.model} and price is {self._price}'

    @property
    def price(self):
        return self._price
    
    @price.setter
    
    def price(self,new_price):
        self._price = max(new_price,0)
        


        


phone1 = Phone('Nokia','1100',1000)

phone1._price = -500
print(phone1.price)
print(phone1.complete_specs)

print(phone1.price)









