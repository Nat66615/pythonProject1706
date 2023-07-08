import socket

# Создаем порт ТСР
client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

#устанавливаем адрес и порт соединения
server_address = ('127.0.0.1', 8080)

# Подключаемся к серверу
client_socket.connect(server_address)

while True:
    # Вводим сообщение для отправки
    massage = input('Введите сообщение (для выхода используйте "exit"): ')

    if massage == 'exit':
        break

    # Отправляем сообщение серверу
    client_socket.send(massage.encode('utf-8'))

    # Получаем ответ от сервера
    responce = client_socket.recv(1024).decode('utf-8')

    print('Получение от сервера: ', responce)

# Закрываем соединение с сервером
client_socket.close()