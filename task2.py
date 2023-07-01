class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def print_info(self):
        print(f'Студент {self.name} возраст {self.age} средний балл {self.gpa}')


student1 = Student('Иванов Иван', 20, 4.8)
student2 = Student('Сергеев Сергей', 19, 4.9)
student3 = Student('Александров Юрий', 21, 3.8)

student1.print_info()
student2.print_info()
student3.print_info()
