class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def make_a_call(self, phone_number):
        print(f'Calling {phone_number} ')

    def full_name(self):
        return f'Your phone is {self.brand} {self.model} '


class Smart_phone(Phone):
    def __init__(self, brand, model, price, ram, rear_cam):

        # Phone.__init__(self,brand,model,price) # not used more
        super().__init__(brand, model, price)  # use more than previous one

        self.ram = ram
        self.rear_cam = rear_cam


phone1 = Phone('nokia', 1100, 1000)
smart_phone = Smart_phone('one+', '6', 45000, '6gb', '48mp')

print(phone1.brand)
print(smart_phone.brand)













