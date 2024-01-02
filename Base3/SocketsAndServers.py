import socket

with socket.socket() as s: s.connect(('127.0.0.1', 9990)); s.send(b'Knock, knock'); print("Server Response:", s.recv(1024).decode())
