import random


class Character:
    def __init__(self, name, health, attack ):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage

    def attack_target(self, target):
        damage = random.randint(1, self.attack)
        print(f'{self.name} атакует {target.name} и наносит {damage} урона')
        target.take_damage(damage)


class Player(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.portions = 3

    def use_portions(self):
        if self.portions > 0:
            self.health += 20
            self.portions -= 1
            print(f'{self.name} использует'
                  f' зелье и восстанавливает 20 здоровья')
        else:
            print('нет зелья')

class Enemy(Character):
    pass

player = Player('Герой', 100, 20)
enemy = Enemy('Монстр', 50, 10)

print('Добро пожаловать в консольную RPG')

#Основной цикл игры
while player.is_alive() and enemy.is_alive():
    print(f'{player.name}: Здоровье - {player.health}'
          f'Лечебное зелье - {player.portions}')
    print(f'{enemy.name}: Здоровье - {enemy.health}')

    choice = input('1 - Атаковать\n'
                   '2 - Использовать зелье\n'
                   '(1-2):')
    if choice == '1':
        player.attack_target(enemy)
        if not enemy.is_alive():
            print(f'{enemy.name} повержен')
    elif choice == 2:
        player.use_portions()
    else:
        print('выбор не верен')

    if enemy.is_alive():
        enemy.attack_target(player)
        if not player.is_alive():
            print(f'{player.name} погиб!')

print('Конец игры')
if player.is_alive():
    print('Вы победили')
else:
    print('Вы проиграли!')

