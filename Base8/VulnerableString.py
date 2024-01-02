import socket as s
from io import BytesIO
import gzip

client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(('localhost', 10000))
client.send(b'GET_KEY')
data = client.recv(4096)
file = gzip.GzipFile(fileobj=BytesIO(data))
print(file.read())

client.close()