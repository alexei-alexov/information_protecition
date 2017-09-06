import string


def additive_cipher(data, key, alph=string.ascii_uppercase):
    try:
        a_len = len(alph)
        return "".join([alph[(alph.find(c)+key) % a_len] if alph.find(c) != -1 else c for c in data])
    except Exception, err:
        return "error: ", err


def multiply_cipher(data, key, alph=string.ascii_uppercase):
    try:
        a_len = len(alph)
        return "".join([alph[(alph.find(c)*key) % a_len] if alph.find(c) != -1 else c for c in data])
    except Exception, err:
        return "error: ", err

def alpfine_cipher(data, key1, key2, alph=string.ascii_uppercase):
    try:
        a_len = len(alph)
        return "".join([alph[(alph.find(c)*key1 + key2) % a_len] if alph.find(c) != -1 else c for c in data])
    except Exception, err:
        return "error: ", err

def additive_uncipher(data, key, alph=string.ascii_uppercase):
    try:
        a_len = len(alph)
        return "".join([alph[(a_len + alph.find(c) - key) % a_len] if alph.find(c) != -1 else c for c in data])
    except Exception, err:
        return "error: ", err


def multiply_uncipher(data, key, alph=string.ascii_uppercase):
    try:
        a_len = len(alph)
        return "".join([alph[(alph.find(c) / key) % a_len] if alph.find(c) != -1 else c for c in data])
    except Exception, err:
        return "error: ", err

def alpfine_uncipher(data, key1, key2, alph=string.ascii_uppercase):
    try:
        a_len = len(alph)
        return "".join([alph[((alph.find(c) - key2) / key1 ) % a_len] if alph.find(c) != -1 else c for c in data])
    except Exception, err:
        return "error: ", err


print string.ascii_uppercase



print additive_cipher("test string".upper(), 8)
print additive_uncipher(additive_cipher("test string".upper(), 8), 8)
print multiply_cipher("test string".upper(), 11)
print multiply_uncipher(multiply_cipher("test string".upper(), 11), 11)
print alpfine_cipher("test string".upper(), 11, 8)
print alpfine_uncipher( alpfine_cipher("test string".upper(), 11, 8), 11, 8)
