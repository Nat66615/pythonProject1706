import socket
import threading


# Функция для обработки подключенного клиента
def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(f'{client_address[0]}: {client_address[1]}]: {message}')
            broadcast(message, client_socket)

        except:
            # Если возника ошибка
            remove_client(client_socket)
            break

# Функция для отправки сообщения всем клиентам
def broadcast(message, sender_socket):
    for cleint in clients:
        if cleint != sender_socket:
            try:
                cleint.send(message.encode('utf-8'))
            except:
                remove_client(cleint)

# Функция для удаления клиента из списка
def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)


# Создание ТСР сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Получение IP-адреса сервера и порта
server_address = input('Введите IP-адрес сервера: ')
server_port = int(input('Введите порт сервера: '))


# Привязать сервера к заданному адресу и порту
server_socket.bind((server_address, server_port))

# Список клиентских сокетов
clients = []

# Отлаживание подключения клиентов
server_socket.listen(5)
print('Сервер запущен. Ожидание подключений...')

# Основной цикл сервера
while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    print(f'Клиент подключен [{client_address[0]}:{client_address[1]}] ')
    client_thread = threading.Thread(
        target=handle_client,
        args=(client_socket, client_address)
    )
    client_thread.start()