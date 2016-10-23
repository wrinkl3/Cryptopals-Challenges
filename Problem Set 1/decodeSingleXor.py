#!/usr/bin/python3

import sys, codecs, binascii

def applyKey(c, key):
	res = [chr(x^key) for x in c]
	return ''.join(res)

freq = "ETAOINSHRDLU"

def score(text):
	score = 0
	for i in range(len(freq)):
		charCoeff = len(freq)-i
		score = score + text.count(freq[i])*charCoeff
	return score

def decodeXor(cyphertext):
	c = bytearray.fromhex(cyphertext)
	plains = [applyKey(c, key) for key in range(256)]
	highest = max([(plain, score(plain)) for plain in plains], key = lambda x:x[1])
	
	return highest	

def main():
	print(decodeXor(sys.argv[1])[0])

if __name__ == "__main__":
    main()