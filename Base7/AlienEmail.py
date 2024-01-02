import os

for root, dirs, files in os.walk('/tmp'):
	for file in files:
		with open(os.path.join('/tmp', file), 'rb') as f:
			if b'PNG' in f.read(4):
				print(f.read())