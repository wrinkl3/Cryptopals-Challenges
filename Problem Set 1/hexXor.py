#!/usr/bin/python3

import sys

def hexXor(x, y):
	if len(x) != len(y):
		print("Oh noes! Strings not equal!")
		sys.exit()
	xor = hex(int(x, 16)^int(y, 16))
	return xor.lstrip('0x')

def main():
	x, y = sys.argv[1], sys.argv[2]
	print(hexXor(x, y))


if __name__ == "__main__":
    main()