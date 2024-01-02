import socket as s


def xor(str1, str2):
	return bytearray(a^b for a,b in zip(*map(bytearray, [str1, str2])))

def debugMsg(msg):
  with open("/tmp/userdebug.log", "a") as myfile:
    myfile.write(msg + "\\n")

server = s.socket(s.AF_INET, s.SOCK_STREAM)
server.bind(('localhost', 10000))
server.listen(1)
while True:
	conn, addr = server.accept()
	msg = conn.recv(1024)
	decoded = xor(msg, bytes("attackthehumans", 'utf-8'))
	conn.send(decoded)
	decoded = decoded.decode()
	print(conn.recv(4096).decode())
	if len(msg) > 0:
		break

server.close()