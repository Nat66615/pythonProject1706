class MyClass:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print('Привет, ' + self.name + '!')


m = MyClass('Андрей')
m.hello()

print(m.__dict__)


class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def speak(self):
        print('Я говорю')


class Dog(Animal):
    def speak(self):
        print('Гав-Гав')


class Cat(Animal):
    def speak(self):
        print('Мур-мяу')


dog = Dog('Ричард')
dog.speak()
#dog.dog_speak()

cat = Cat('Чарли')
cat.speak()

print(dog.__dict__)
print(cat.__dict__)


class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2


rectangle = Rectangle(4, 5)
print(rectangle.area())

circle = Circle(3)
print(circle.area())
