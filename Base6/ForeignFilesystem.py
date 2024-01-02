import os

directory = '/tmp/aliendir'
for root, dirs, files in os.walk(directory):
	for file in files:
		print(file)