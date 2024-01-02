with open('/tmp/destroymoonbase.gif', 'rb') as f:
	data = str(f.read(), 'utf-8')
	data = data.replace('#', "").replace('$', "")
	print(data)