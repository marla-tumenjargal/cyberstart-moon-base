import urllib.request


while True:
	res = urllib.request.urlopen('http://127.0.0.1:8082/selfdestruct')
	data = str(res.read(), 'utf-8')
	if 'Win: ' in data:
		print(data)
		break