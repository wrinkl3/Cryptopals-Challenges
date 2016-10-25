#!/usr/bin/python3

import sys, base64, itertools
from decodeSingleXor import decodeXor
from repeatingKeyXor import repeatXor

MIN_KEYSIZE = 2
MAX_KEYSIZE = 40
NUM_CANDIDATES = 3

def popCount(b):
    return sum([(b>>i)&1 for i in range(8)])

def binHammingDistance(s1, s2):
	if len(s1) != len(s2):
		raise ValueError("Oh noes! Strings not equal length!")
	return sum([popCount(b1^b2) for b1, b2 in zip(s1, s2)])

def findKeySizeCandidates(text):
	samples = [(text[:keysize], text[keysize:2*keysize], keysize) for keysize in range(MIN_KEYSIZE, MAX_KEYSIZE)]
	distances = sorted([(binHammingDistance(sample[0], sample[1])/sample[2], sample[2]) for sample in samples], key=lambda x: x[0])
	candidates = [cand[1] for cand in distances[:NUM_CANDIDATES]]
	return candidates

def splitIntoBlocks(text, blockSize):
	#print([text[i:i+blockSize] for i in range(0, len(text), blockSize)])
	return [text[i:i+blockSize] for i in range(0, len(text), blockSize)]

def transposeBlocks(blocks):
	return(list(itertools.zip_longest(*blocks, fillvalue=0)))

def decodeUsingCandidate(cipherText, candidate):
	transBlocks = transposeBlocks(splitIntoBlocks(cipherText, candidate))
	#print(len(transBlocks))
	#print(transBlocks)
	#print(type(transBlocks))
	#for block in transBlocks:
	#	print(block)
	decodedBlocks = [decodeXor(bytes(block))[2] for block in transBlocks]
	print(decodedBlocks)
	key = bytes(decodedBlocks)
	return key

def main():
	f = open(sys.argv[1], encoding='utf-8')
	cipherText = base64.b64decode(''.join(f.read()).replace('\n', ''))
	f.close()
	candidates = findKeySizeCandidates(cipherText)
	print(candidates)
	keys = [decodeUsingCandidate(cipherText, c) for c in candidates]
	for k in keys:
		print(repeatXor(k, cipherText))
		print('aaaaaaaaaaaa')
	#print(plainTexts[0])



if __name__ == "__main__":
    main()