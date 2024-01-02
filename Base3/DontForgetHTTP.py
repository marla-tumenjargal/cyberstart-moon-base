import urllib.request

print(urllib.request.urlopen("http://127.0.0.1:8080/winning").read().decode('utf-8'))
