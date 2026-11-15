class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        if self.num2 == 0:
            return "error! division by zero."
        return self.num1 / self.num2
calc = Calculator(10, 5)
print("addtion:", calc.add())
print("subtraction:", calc.subtract())
print("multiplication:", calc.multiply())
print("division:", calc.divide()