
# instance and class variables are different, instance variable can on the value we pass to the constructor in line: 20
class Calculator:
    num = 100  # class variable
    # default constructor

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        print("default constructor")

    # methods
    def getData(self):
        print("inside a method")

    def addition(self):
        return self.a + self.b + Calculator.num  # we can also write self.num


obj = Calculator(12, 14)  # creating object
obj.getData()
print(obj.addition())  # 126

obj = Calculator(12, 20)  # creating object, second instance
obj.getData()
print(obj.addition())  # 132
