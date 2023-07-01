class Calculator:
    def __init__(self, num_a, num_b):
        self.num_a = num_a
        self.num_b = num_b

    def addition(self):
        return self.num_a + self.num_b

    def subtraction(self):
        return self.num_a - self.num_b

    def multiplication(self):
        return self.num_a * self.num_b

    def division(self):
        return self.num_a / self.num_b


obj1 = Calculator(25, 47)
print(f'Результат сложения {obj1.num_a} и {obj1.num_b} - {obj1.addition()}')
print(obj1.subtraction())
print(obj1.multiplication())
print(obj1.division())