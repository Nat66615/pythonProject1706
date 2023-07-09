import socket
import threading

# Хост и порт сервера
HOST = '127.0.0.1'
PORT = 8000

# Создание сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключение к серверу
client_socket.connect((HOST, PORT))

# Получение приветственного сообщения от сервера
welcome_massage = client_socket.recv(1024).decode()
print(welcome_massage)

# Функция для отправки координат выстрела на сервер
def send_shot_coordinates(coordinates):
    client_socket.send(coordinates.encode())

# Функция для получения и отображения состояния игрового поля
def receive_board_state():
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(data)

# Запуск потока для получения и отображения состояния игрового поля
board_thread = threading.Thread(target=receive_board_state)
board_thread.start()

# Пример взаимодействия с пользователем
while True:
    coordinates = input('Введите координаты выстрела (например, А1): ')
    send_shot_coordinates(coordinates)