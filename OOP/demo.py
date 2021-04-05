

class laptop:
    def __int__(self,model,price,processor):
        self.model = model
        self.price = price
        self.processor = processor

    def apply_discount(self,percentage):
        discount = self.price - ((self.price*percentage)/100)
        return discount



laptop_one = laptop('thinkpad t450',64000,'i7 5th gen')
print(laptop_one.price)
print(laptop_one.apply_discount(20))











