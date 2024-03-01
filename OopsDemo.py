#self keyword is mandatory for calling instance varible names into method
#instance and class variable have whole different purpose
#constructor name should be be  __init__
#new keyword is not required when you create object

class Calculator:
    num = 100  # class variables

    #default constructor
    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called when object is created")

    def getdata(self):
        print("I am executing as method in class")

    def summation(self):
        return self.firstNumber+self.secondNumber + self.num


obj=Calculator(3,4)
print(obj.summation())
obj.getdata()
print(obj.num)
