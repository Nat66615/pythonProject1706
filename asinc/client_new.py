import socket
import threading


# Функция для приема сообщений от сервера
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            client_socket.close()
            break


# Функция для отправки сообщений на сервер
def send_message(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))


# Функция  подключения к серверу
def connect_to_server():
    sever_address = input('Введите IP-адрес сервера: ')
    server_port = int(input('Введите порт: '))

    # Создаем сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((sever_address, server_port))

        receive_thread = threading.Thread(
            target=receive_messages,
            args=(client_socket,)
        )
        send_thread = threading.Thread(
            target=send_message,
            args=(client_socket,)
        )
        receive_thread.start()
        send_thread.start()
    except:
        print('Ошибка подключения!')


# Запуск
connect_to_server()
