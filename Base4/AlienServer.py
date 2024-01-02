import socket

def send_receive(value):
    sock.sendall(value)
    response = sock.recv(1024)
    print("Response from {value.decode()}: {response.decode()}")

with socket.create_connection(('localhost', 10000)) as sock:
    values = [b'USER', b'aliensignal', b'PASS', b'unlockserver', b'SEND', b'moonbase', b'END']
    for value in values:
        send_receive(value)