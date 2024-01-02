import socket as s
import string

client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(('localhost', 10000))
client.send(b'Hello World')
word_codes = client.recv(4096) 
strWordCodes = str(word_codes, 'utf-8') 

f = open('backdoor.txt', 'r')
content = f.read().split("\n\n")

wordList = []
data = strWordCodes.split("\n")[:-1] 
for item in data: 
	row = item.split(",")
	paragraph_number, line_number, word_number = [x for x in row]
	print(paragraph_number, line_number, word_number)
  
	PARAGRAPH_TEXT = content[int(paragraph_number)-1]
	paragraphLines = PARAGRAPH_TEXT.split('\n')
	for ind, line in enumerate(paragraphLines):
		print(ind+1, line)
   
	LINE_TEXT = paragraphLines[int(line_number)-1]
	lineWords = LINE_TEXT.split(" ")
	print("LINE: " + LINE_TEXT)
  
	WORD = lineWords[int(word_number)-1]
	puncList = [x for x in string.punctuation]
	for c in WORD:
		if c in puncList:
			WORD = WORD.replace(c, "")
	wordList.append(WORD)
	print("WORD: " + WORD)
	print()
  
replyStr = ''
for word in wordList:
	replyStr = replyStr + word + '\n'
  
print(replyStr)
client.send(replyStr.encode())
print(str(client.recv(4096), 'utf-8'))