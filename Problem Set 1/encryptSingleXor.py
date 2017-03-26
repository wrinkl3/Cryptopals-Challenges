import sys, base64, codecs

def applyKey(c, key):
	res = [chr(x^key) for x in c]
	return ''.join(res)

def encryptBytes(plain, key):
	ret =  applyKey(plain, key)
	return bytes(ret, 'utf-8')


def encryptString(string, key):
	b1 = bytearray()
	b1.extend(string.encode())
	return encryptBytes(b1, ord(key))


def main():
	res = encryptString(sys.argv[1], sys.argv[2])
	print(codecs.encode(res, 'hex'))

if __name__ == "__main__":
    main()