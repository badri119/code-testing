class Calculator:
    num = 100 #class vatiable

    #default constructor
    def __init__(self, a, b):
        self.a = a #method variable
        self.b = b #method variable
        # print('I am called automatically')


    def sum(self):
        return self.a + self.b + Calculator.num


obj = Calculator(2,3) #syntax to create objects in python
print(obj.sum())

obj1 = Calculator(6,3) #syntax to create objects in python
print(obj1.sum())
