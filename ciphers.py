import string


def additive_cipher(data, key, alph=string.ascii_uppercase):
    try:
        print "DATA: ", data
	print "KEY: ", key
        a_len = len(alph)
        return "".join([alph[(alph.find(c)+key) % a_len] if alph.index(c) != -1 else c for c in data])
    except Exception, err:
        return "error: ", err

print string.ascii_uppercase
print additive_cipher("test string".upper(), 1)
print additive_cipher("test string".upper(), 3)
print additive_cipher("test string".upper(), 8)
