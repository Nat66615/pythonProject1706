class Employee:

    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.position = args[2]
        self.salary = args[3]

       #self.name, self. age, self.position, self.salary = args
    def get_name(self):
        return self.name

    def set_name(self):
        self.name = input('Введите имя: ')

    def get_age(self):
        return self.age

    def set_age(self):
        self.age = input('Укажите возраст: ')

    def get_salary(self):
        return self.salary

    def set_salary(self):
        self.salary = int(input('Укажите ЗП: '))

    def up_salary(self):
        procent = int(input(": "))
        self.salary = self.salary + self.salary * (procent / 100)

employee = Employee('Иван', 30, 'Уборщик', 1000)

print(employee.get_name(), '\n', employee.get_age(), '\n', employee.get_salary())

#поднять зарплату
employee.up_salary()
print(employee.salary)