import urllib.request, urllib.parse

header = {'x-api-key': 'tweetbotkeyv1'}

# querystring data containing user=tweetbotuser and status-update=alientest
params = {'user': 'tweetbotuser', 'status-update': 'alientest'}
querystring = urllib.parse.urlencode(params)

req = urllib.request.Request('http://127.0.0.1:8082', data=bytes(querystring, 'utf-8'), method='POST', headers=header)
res = urllib.request.urlopen(req)
print(res.read())