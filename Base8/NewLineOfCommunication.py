import socket as s
from collections import Counter
        
def crackW(input):
	possibleOutput = ''
	maxPoints = 0 
	tempPoints = 0
	inputArr = input.split(" ")
  
	for i in range(0, 26):
		output = ""
		list_len = len(inputArr)-1
		for index, word in enumerate(inputArr):
			for j in range(len(word)):
				char = word[j]
				newChar = chr((ord(char) + i - 65) % 26 + 65)
				output += newChar
			if index != list_len:
				output = output + " "

		MOST_FREQ_CHARS = ['E', 'T', 'A', 'O', 'S', 'H', 'I']
		freqChar, freqList = findMaxFreq(output)
    
		if [c in str(freqList) for c in MOST_FREQ_CHARS]:
			for ch, val in freqList:
				if ch in MOST_FREQ_CHARS: 
					tempPoints = tempPoints + val
		if tempPoints >= maxPoints:
			maxPoints = tempPoints
			possibleOutput = output
		tempPoints = 0
	output = possibleOutput
	return output
    
def findMaxFreq(input):
	counter = Counter(input)
	keys = sorted(counter, key=counter.get, reverse=True)
	res = keys[1] if keys[0] == ' ' else keys[0]
	most_common = counter.most_common(6)[1:]
	return (res, most_common)
    
client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(('localhost', 10000))
client.send(b'GET')
data = client.recv(1024)
dataMsgs = data.split(b'\n')

msg1 = dataMsgs[1].decode()
msg2 = dataMsgs[2].decode()
msg3 = dataMsgs[3].decode()

print(data)
print()

decoded1 = crackW(msg1)
decoded2 = crackW(msg2)
decoded3 = crackW(msg3)

decodedMsg = decoded1 + "\n" + decoded2 + "\n" + decoded3 + "\n"
decodedMsgStr = decodedMsg.encode()
print(decodedMsgStr)
client.send(decodedMsgStr)
print(client.recv(4096).decode())

client.close()