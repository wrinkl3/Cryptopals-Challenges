#!/usr/bin/python3

import sys

def applyKey(c, key):
	res = [chr(x^key) for x in c]
	return ''.join(res)

#freq = "ETAOINSHRDLU"
freq = dict()
freq['a']=834
freq['b']=154
freq['c']=273
freq['d']=414
freq['e']=1260
freq['f']=203
freq['g']=192
freq['h']=611
freq['i']=671
freq['j']=23
freq['k']=87
freq['l']=424
freq['m']=253
freq['n']=680
freq['o']=770
freq['p']=166
freq['q']=9
freq['r']=568
freq['s']=611
freq['t']=937
freq['u']=285
freq['v']=106
freq['w']=234
freq['x']=20
freq['y']=204
freq['z']=6
freq[' ']=2320

def score(text):
	score = 0
	for c in text.lower():
		if c in freq:
			score+=freq[c]
	return score

def decodeXor(c):
	plains = [(applyKey(c, key), key) for key in range(256)]
	highest = max([(plain[0], score(plain[0]), plain[1]) for plain in plains], key = lambda x:x[1])
	
	return highest

def decodeXorFromString(cyphertext):
	return decodeXor(bytearray.fromhex(cyphertext))	

def main():
	print(decodeXorFromString(sys.argv[1])[0])

if __name__ == "__main__":
    main()