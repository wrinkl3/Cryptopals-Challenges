#!/usr/bin/python3

import sys
from decodeSingleXor import decodeXor

MIN_KEYSIZE = 2
MAX_KEYSIZE = 40
NUM_CANDIDATES = 3

def popCount(b):
    return sum([(b>>i)&1 for i in range(8)])

def binHammingDistance(s1, s2):
	binarr1, binarr2 = bytearray(s1, 'utf-8'), bytearray(s2, 'utf-8')
	if len(binarr1) != len(binarr2):
		raise ValueError("Oh noes! Strings not equal length!")
	return sum([popCount(b1^b2) for b1, b2 in zip(binarr1, binarr2)])

def findKeySizeCandidates(textSample):
	samples = [(textSample[:keysize], textSample[keysize:2*keysize], keysize) for keysize in range(MIN_KEYSIZE, MAX_KEYSIZE)]
	distances = sorted([(binHammingDistance(sample[0], sample[1])/sample[2], sample[2]) for sample in samples], key=lambda x: x[0])
	candidates = [cand[1] for cand in distances[:NUM_CANDIDATES]]
	return candidates

def splitIntoBlocks(text, blockSize):
	return [text[i:i+blockSize] for i in range(0, len(text), blockSize)]

def transposeBlocks(blocks):
	return [''.join(block) for block in zip(*blocks)]

def decodeUsingCandidate(cipherText, candidate):
	transBlocks = transposeBlocks(splitIntoBlocks(cipherText, candidate))
	transDecoded = [decodeXor(block) for block in transBlocks]
	decodedBlocks = transBlocks(transDecoded)
	plainText = ''.join(decodedBlocks)
	return plainText

def main():
	f = open(sys.argv[1], encoding='utf-8')
	candidates = findKeySizeCandidates(f.read(MAX_KEYSIZE*2).strip('\n'))
	cipherText = f.read()
	f.close()
	plainTexts = [decodeUsingCandidate(cipherText, c) for c in candidates]
	print(plainTexts[0])



if __name__ == "__main__":
    main()