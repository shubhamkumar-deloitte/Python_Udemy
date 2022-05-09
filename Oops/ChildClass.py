from Oops.Inheritance import Calculator


class Child(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)  # invoking the constructor of parent class and passing the required parameters
        print("constructor of Child class")

    def getCompleteData(self):
        return self.num2 + self.num + self.addition()


obj = Child()
print(obj.getCompleteData())
