#!/usr/bin/python3

import sys, binascii

def popCount(b):
    return sum([(b>>i)&1 for i in range(8)])

def binHammingDistance(s1, s2):
	binarr1, binarr2 = bytearray(s1, 'utf-8'), bytearray(s2, 'utf-8')
	if len(binarr1) != len(binarr2):
		raise ValueError("Oh noes! Strings not equal length!")
	return sum([popCount(b1^b2) for b1, b2 in zip(binarr1, binarr2)])

def main():
	f = open(sys.argv[1], encoding='utf-8')



if __name__ == "__main__":
    main()