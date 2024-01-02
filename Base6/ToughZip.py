import zipfile

file = '/tmp/alien-sample-42.zip'
possiblePasswordList = [
  'pant', 'papa', 'paps', 'para', 'path', 'pats', 'paty',
  'pard', 'pare', 'park', 'parr', 'pars', 'part', 'pase',
  'pash', 'past', 'pate', 'peal', 'pean', 'pear', 'peas',
  'pave', 'pawl', 'pawn', 'paws', 'pays', 'peag', 'peak',
  'peck', 'pele', 'peat', 'pech', 'peke', 'perm', 'perp',
  'pecs', 'peds', 'peed', 'peek', 'peel', 'peen', 'peep',
  'pelf', 'pelt', 'pend', 'pens', 'pent', 'pass', 'pepo',
  'pert', 'phon', 'phot', 'phut', 'peer', 'pegs', 'pehs',
  'pere', 'peri', 'perk', 'phat', 'phew', 'phis', 'phiz',
  'perv', 'peso', 'pest', 'pets', 'pews', 'pfft', 'pfui',
  'pial', 'pian', 'pias', 'pica', 'pice', 'pick', 'pics',
  'pied', 'pier', 'pies', 'pigs', 'plan', 'plat', 'ploy',
  'pika', 'pike', 'piki', 'pint', 'piny', 'pion', 'pith',
  'pile', 'pili', 'pill', 'pily', 'pima', 'pimp', 'pina',
  'pine', 'ping', 'pink', 'pins', 'plug', 'plum', 'pein',
  'poll', 'peps', 'pits', 'pity', 'pixy', 'plop', 'plot',
  'pipe', 'pips', 'pipy', 'pirn', 'pish', 'piso', 'pita',
  'pole', 'plow', 'plod', 'pois', 'poke', 'poky',
  'play', 'plea', 'pleb', 'pled', 'plew', 'plex', 'plie',
  'plus', 'pock', 'poco', 'pods', 'poem', 'poet', 'pogy',
]

with zipfile.ZipFile(file) as archive:
	for i in range(0, len(possiblePasswordList)):
		try:
			passAttempt = bytes(possiblePasswordList[i], 'utf-8')
			archive.extractall(path='/tmp', pwd=passAttempt)
			break
		except RuntimeError:
			continue