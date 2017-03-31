#!/usr/bin/python3

import sys, codecs

def repeatXor(key, text):
	return bytes([text[i]^key[i%len(key)] for i in range(len(text))])

def main():
	key = bytes(sys.argv[1], 'utf-8')
	text = bytes(sys.argv[2], 'utf-8')
	cipher = repeatXor(key, text)
	print(codecs.encode(cipher, 'hex').decode('ascii'))

if __name__ == "__main__":
    main()