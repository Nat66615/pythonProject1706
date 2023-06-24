import random


class Character:
    def __init__(self, name, health, attack):
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


def print_turn(func):
    def wrapper(*args, **kwargs):
        print('===== Начало хода =====')
        result = func(*args, **kwargs)
        print('===== Конец функции =====')
        return result

    return wrapper


def random_damage(func):
    def wrapper(*args, **kwargs):
        damage = random.randint(1, 10)
        print(f'урон: {damage}')
        kwargs['damage'] = damage
        return func(*args, **kwargs)

    return wrapper


def check_alive(func):
    def wrapper(*args, **kwargs):
        if args[0].is_alive():
            return func(*args, **kwargs)
        else:
            print('Персонаж мертв!')

    return wrapper


def print_action(func):
    def wrapper(*args, **kwargs):
        action_name = func.__name__.replace('_', ' ').capitalize()
        print(f'{args[0].name} выбрал действие: {action_name}')
        return func(*args, **kwargs)

    return wrapper

@print_turn
@print_action
@check_alive
@random_damage
def attack_target(attacker, target, damage):
    target.take_damage(damage)


@print_turn
@print_action
@check_alive
def use_portions(player):
    player.use_portions()


player = Player('Герой', 100, 20)
enemy = Enemy('Монстр', 50, 10)

print('Добро пожаловать в консольную RPG')

# Основной цикл игры
while player.is_alive() and enemy.is_alive():
    print(f'{player.name}: Здоровье - {player.health}'
          f'Лечебное зелье - {player.portions}')
    print(f'{enemy.name}: Здоровье - {enemy.health}')

    choice = input('1 - Атаковать\n'
                   '2 - Использовать зелье\n'
                   '(1-2):')
    if choice == '1':
        attack_target(player, enemy)
        if not enemy.is_alive():
            print(f'{enemy.name} повержен')
    elif choice == 2:
        player.use_portions()
    else:
        print('выбор не верен')

    if enemy.is_alive():
        attack_target(enemy, player)
        if not player.is_alive():
            print(f'{player.name} погиб!')

print('Конец игры')
if player.is_alive():
    print('Вы победили')
else:
    print('Вы проиграли!')
