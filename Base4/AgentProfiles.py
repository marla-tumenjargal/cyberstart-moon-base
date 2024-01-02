import os.path

count = 1
flag = ""

for i in range(20):
	fname = "/tmp/agent-" + str(count)+".txt"
	if os.path.isfile(fname):
		with open(fname, 'r') as content_file:
			content = content_file.read()
			content = content.rstrip()
			flag = flag + content
	count += 1

print(flag)