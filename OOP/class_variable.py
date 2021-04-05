# class variable

# make a circle class and calculate the area and circumference

class Circle:

    # class Variable
    pi = 3.14

    def __init__(self,radius):
        self.radius = radius
        

    def calc_area(self):
        return Circle.pi*(self.radius**2)
    
    def calc_circum(self):
        return 2*Circle.pi*self.radius


Circle_1 = Circle(5)
Circle_2 = Circle(6)

print(Circle_1.calc_area())
print(Circle_2.calc_area())















