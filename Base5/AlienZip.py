import os
import zipfile 


def inc(codeStr):
	return str(int(codeStr)+1).zfill(len(codeStr))

with zipfile.ZipFile('/tmp/alien-zip-2092.zip') as archive:
	while int(code) < 1000:
		try:
			archive.extract(member='alien-zip-2092.txt', path='/tmp', pwd=bytes(000, 'utf-8'))
			code = inc(code)
			break
		except RuntimeError:
			code = inc(code)
			continue