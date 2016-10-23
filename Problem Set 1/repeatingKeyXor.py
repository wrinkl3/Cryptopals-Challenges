#!/usr/bin/python3

text = "Burning 'em, if you ain't quick and nimble"
key = "ICE"

def main():

	def xor_bytes(b1, b2):
		return hex(ord(b1)^ord(b2)).replace('0x', '')

	c = ''.join(xor_bytes(text[i], key[i%len(key)]) for i in range(len(text)))

	print(c)

if __name__ == "__main__":
    main()