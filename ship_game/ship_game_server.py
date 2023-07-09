import socket
import threading
import random

# Хост и порт сервера
HOST = '127.0.0.1'
PORT = 8000

# Создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязка сокета к хосту и порту
server_socket.bind((HOST, PORT))

# Ожидание подключения клиентов
server_socket.listen(2)
print('Ожидание подключений...')

# Списо подключенных клиентов
clients = []

# Размер игрового поля
BOARD_SISE = 10

# Игровое поле с кораблями
board = [
    [' ' for _ in range(BOARD_SISE)] for _ in range(BOARD_SISE)
]

# Блокировка поступа к игровому полю
board_lock = threading.Lock()


# Функция обработки клиента
def handle_client(client_socket, client_address):
    # Добавление клиента в список
    clients.append(client_socket)

    # Отправка приветственного сообщения клиенту
    client_socket.send('Добро пожаловать в игру "Морской бой"!'.encode('utf-8'))

    # Обработка ходов клиента
    while True:
        try:
            # Получение координат выстрела от клиента
            data = client_socket.recv(1024).decode()
            if not data:
                break

            # Обработка полученных координат (логика игры)
            process_shot(data)

            # Отправка обновленного состояния игрового поля клиент
            send_board_state()

        except:
            break

    # закрытие соединения с клиентом
    client_socket.close()
    print(f'Клиент {client_address} отключен')


# Функция обрботки выстрела
def process_shot(coordinates):
    with board_lock:
        x, y = parse_coordinates(coordinates)
        if x is not None and y is not None:
            if board[x][y] == ' ':
                board[x][y] = 'o'
            elif board[x][y] == 'X':
                board[x][y] = '#'


# Функция отправки обновленного состояния игрового поля
def send_board_state():
    with board_lock:
        board_state = '\n'.join([' '.join(row) for row in board])
        for client in clients:
            client.send(board_state.encode())


# Функция для преобразования координат в индексы игрового поля
def parse_coordinates(coordinates):
    try:
        x = ord(coordinates[0].upper()) - ord('A')
        y = int(coordinates[1:]) - 1
        if x < 0 or x >= BOARD_SISE or y < 0 or y >= BOARD_SISE:
            raise ValueError
        return x, y
    except:
        return None, None


# Функция для случайного размещкния кораблей на игровом поле
def place_ships():
    ship_sizes = [5, 4, 3, 3, 2]
    for size in ship_sizes:
        while True:
            x = random.randint(0, BOARD_SISE - 1)
            y = random.randint(0, BOARD_SISE - 1)
            orientation = random.choice(['Горизонталь', 'Вертикаль'])
            if is_valid_ship_placement(x, y, size, orientation):
                break

        if orientation == 'Горизонталь':
            for i in range(size):
                board[x][y + 1] = 'X'
        else:
            for i in range(size):
                board[x + 1][y] = 'X'


# Функция для проверки возможности размещения корабля на игровом поле
def is_valid_ship_placement(x, y, size, orientation):
    if orientation == 'Горизонталь':
        for i in range(size):
            if y + 1 >= BOARD_SISE or board[x][y + 1] != ' ':
                return False
    else:
        for i in range(size):
            if x + i >= BOARD_SISE or board[x + i][y] != ' ':
                return False
    return True


# Вызов функции для случайного размещения кораблей на игровом полe
place_ships()

# Ожидание подключений клиентов
while True:
    client_socket, client_address = server_socket.accept()
    print(f'Новое подключение от {client_address}')

    # Запуск потока для обработки клиента
    client_thread = threading.Thread(
        target=handle_client,
        args=(client_socket, client_address)
    )
    client_thread.start()
