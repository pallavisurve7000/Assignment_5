# implement a calculator class

class Calculator:

    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2
    def add(self):
        print("Addition :",self.no1 + self.no2)
    def subtract(self):
        if self.no1 < self.no2:
            print("Subtraction :",self.no2 - self.no1)
        else:
            print("Subtraction :",self.no1 - self.no2)
    def multiply(self):
        print("Multiplication :",self.no1 * self.no2)
    def divide(self):
        if self.no1 < self.no2:
            print("Division :",self.no2 / self.no1)
        else:
            print("Division :",self.no1 / self.no2)

no1 = int(input("Enter the first number :"))
no2 = int(input("Enter the second number :"))
print(f"The first number : {no1} \n The second number {no2}")
obj = Calculator(no1,no2)
obj.add()
obj.subtract()
obj.multiply()
obj.divide()