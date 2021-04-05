
class laptop:
    def __init__(self,model_no,processor,display,webcam,battery):
        self.model_number = model_no
        self.processor = processor
        self.display = display
        self.webcam = webcam
        self.battery = battery
        self.laptop_name = model_no + processor

    


laptop_one= laptop('Thinkpad T450s ','core i7 5th gen','14 iche full hd+ resoulation','hd cam ','4 hours battery life')
laptop_two = laptop('Elitebook 840','Amd rygen 5 4300','15 inch HD plus','Full HD cam','10 hours battery life')


print(laptop_one.model_number)
print(laptop_one.processor)
print(laptop_one.display)
print(laptop_one.webcam)
print(laptop_one.battery)
print(laptop_one.laptop_name)










