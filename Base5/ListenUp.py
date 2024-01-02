import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 10000))
server_socket.listen()

while True:
    conn, addr = server_socket.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024).decode()
        print('Received:', data)

        with open("/tmp/aliensignallog.txt", "a") as signal_log:
            signal_log.write(data + "\n")

        conn.sendall("Signal received successfully")
