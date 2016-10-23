#!/usr/bin/python3

import sys

from decodeSingleXor import decodeXor


def main():
	f = open(sys.argv[1], encoding='utf-8')
	decoded = [decodeXor(l.strip('\n')) for l in f]
	print(max(decoded, key = lambda x:x[1])[0])


if __name__ == "__main__":
    main()