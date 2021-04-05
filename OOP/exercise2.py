

class laptop:
    discount_percentage = 10
    def __init__(self,model_no,processor,price):
        self.model_number = model_no
        self.processor = processor
        self.price = price
        
        
    

    def apply_discount(self):
        discount = self.price - ((self.price * self.discount_percentage)/100)
        return discount
    
    def full_info(self):
        return f'My laptop model number is {self.model_number}.\nIt has {self.processor} processor '

    
        
laptop1 = laptop('thinkpad t450s','i7 5th gen',45000)

laptop2 = laptop('hp au114tx','i5 10th gen',78000)
laptop2.discount_percentage =50
print(laptop2.__dict__)
print(laptop2.apply_discount())












