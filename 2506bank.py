class Account:

    def __init__(self, *args):
        self.balance, self.number, self.owner = args

    def get_balance(self):
        return self.balance

    def set_balance(self):
        self.balance = int(input('Укажите баланс: '))

    def get_number(self):
        return self.number

    def set_number(self):
        self.number = input('Укажите номер счета: ')

    def get_owner(self):
        return self.owner

    def set_owner(self):
        self.owner = input('Укажите владельца: ')

    def replenish(self):
        add = int(input("сумма пополнения: "))
        self.balance = self.balance + add

    def withdraw(self):
        reduce = int(input("сумма снятия: "))
        self.balance = self.balance - reduce

account = Account(5000, 365, 'Некто')
print(account.get_balance(), '\n', account.get_number(), '\n', account.get_owner())

#снять деньги
account.replenish()
print(account.get_balance(), '\n', account.get_number(), '\n', account.get_owner())

#пополнить баланс
account.withdraw()
print(account.get_balance(), '\n', account.get_number(), '\n', account.get_owner())


