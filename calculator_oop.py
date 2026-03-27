class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


calc = Calculator()

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Add:", calc.add(a, b))
print("Subtract:", calc.sub(a, b))
print("Multiply:", calc.mul(a, b))
print("Divide:", calc.div(a, b))
