#!/usr/bin/python3

import sys
import codecs

import base64


def hexToBase64(s):
	b = bytes.fromhex(s)
	return(base64.b64encode(b).decode('ascii'))

def main():
	s = sys.argv[1]
	print(hexToBase64(s))

if __name__ == "__main__":
    main()