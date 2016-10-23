#!/usr/bin/python3

import sys
import codecs

def hexToBase64(s):
	return codecs.encode(codecs.decode(s, "hex"), "base64").decode('utf8').strip('\n')

def main():
	s = sys.argv[1]
	print(s)

if __name__ == "__main__":
    main()