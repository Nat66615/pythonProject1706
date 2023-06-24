class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Привет, меня зовут {self.name}')

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        super().greet()
        print(f'Мне {self.age} лет')


child = Child('Иван', 5)
child.greet()