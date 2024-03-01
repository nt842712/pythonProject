from OopsDemo import Calculator


class ChildImpl(Calculator):
    num2=200

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        Calculator.__init__(self, self.firstNumber, self.secondNumber)

    def getcompletedata(self):
        return self.num2+self.num + self.summation()


obj = ChildImpl(2,10)
print(obj.getcompletedata())
