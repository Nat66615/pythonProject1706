import socket

# Создаем сокет ТСР
server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

# Установка адреса и порта сервера
server_address = ('127.0.0.1', 8080)
server_socket.bind(server_address)

# Слушаем входящие соединения
server_socket.listen(1)

print('Сервер запущен. Ожидание подключения...')

while True:
    # Принимаем входящее соединение
    client_socket, client_address = server_socket.accept()
    print('Подключение клиенсткое соединение: ', client_address)

    while True:
        # Получение данных от клиента
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        print('Сообщение: ', data)

        # отправляем ответ клиенту
        response = 'Сообщение получено: ' + data
        client_socket.send(response.encode('utf-8'))

# Закрываем соединение с клиентом
client_socket.close()

