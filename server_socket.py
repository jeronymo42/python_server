import socket

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)

# IP и порт, которые слушает сокет
serv_sock.bind(('192.168.0.104', 9090))

# Размер очереди входящих сообщений для установленных, но еще не обработанных соединений
backlog = 10

# Сокет "слушает" (не блокирует выполнение)
serv_sock.listen(backlog)

request = 0

while True:
    # Получаем соединение из этой backlog, accept() блокирует дальнейшее выполнение, до появления подключения
    client_sock, client_addr = serv_sock.accept()
    while True:
        data = client_sock.recv(1024)
        if not data:
            break
        client_sock.sendall(b'Hello, world')
        request += 1
        print(request)

    client_sock.close()