import string

from helpers import input, positive_int_validator, boolean_validator,\
    in_list_validator, not_empty_validator


ADD_CIPHER = 'add'
MULT_CIPHER = 'mult'
AFFINE_CIPHER = 'affine'

CIPHERS = (ADD_CIPHER, MULT_CIPHER, AFFINE_CIPHER, )


def find_inverted(n, alphabet_size):
    """
    Return inverted to given number with given alphabet size.
    If there is no inverted number to given raise ValueError.
    """
    result = 1
    while (result * n) % alphabet_size != 1:
        result += 1
        if result > alphabet_size:
            raise ValueError("This key don't have primal pair!")
    return result


def cipherer(data, func):
    try:
        return "".join([func(c) for c in data])
    except:
        return ""


def additive_cipher(data, key, alph=string.ascii_uppercase, reverse=False):
    a_len = len(alph)
    data = data.upper()
    if not reverse:
        func = lambda c: alph[(alph.find(c) + key) % a_len] if alph.find(c) != -1 else c
        return cipherer(data, func)
    else:
        result = []
        for key in xrange(1, len(alph) + 1):
            func = lambda c: alph[(a_len + alph.find(c) - key) % a_len] if alph.find(c) != -1 else c
            result.append((key, cipherer(data, func), ) )
        return result

def multiply_cipher(data, key, alph=string.ascii_uppercase, reverse=False):
    a_len = len(alph)
    if not reverse:
        func = lambda c: alph[(alph.find(c)*key) % a_len] if alph.find(c) != -1 else c
        return cipherer(data.upper(), func)
    else:
        result = []
        for key in xrange(1, len(alph) + 1):
            try:
                inv_key1 = find_inverted(key, a_len)
            except:
                continue
            func = lambda c: alph[(alph.find(c) * inv_key1) % a_len] if alph.find(c) != -1 else c
            result.append((key, cipherer(data, func), ) )
        return result


def affine_cipher(data, key1, key2, alph=string.ascii_uppercase, reverse=False):
    a_len = len(alph)
    data = data.upper()
    if not reverse:
        func = lambda c: alph[(alph.find(c)*key1 + key2) % a_len] if alph.find(c) != -1 else c
        return cipherer(data, func)
    else:
        result = []
        for key1 in xrange(1, len(alph) + 1):
            try:
                inv_key1 = find_inverted(key1, a_len)
            except:
                continue
            for key2 in xrange(1, len(alph) + 1):
                func = lambda c: alph[(inv_key1 * (alph.find(c) - key2)) % a_len] if alph.find(c) != -1 else c
                result.append( (key1, key2, cipherer(data, func)) )
        return result


def main():
    """Default function"""
    key1 = 8
    key2 = key1 + 3

    key1 = input("Enter key1 please", key1, positive_int_validator)
    key2 = input("Enter key2 please", key2, positive_int_validator)

    reverse = input("Reverse?", False, boolean_validator)

    cipher_prompt = "Cipher type:\n%s - additive cipher\n%s - multiplicative cipher\n%s - affine_cipher\n" % (
            ADD_CIPHER, MULT_CIPHER, AFFINE_CIPHER, )

    cipher_str = input(cipher_prompt, ADD_CIPHER, in_list_validator(CIPHERS))
    text = input("Enter data to encrypt / decrypt: ", "test string", not_empty_validator)
    result = "error"
    if cipher_str == ADD_CIPHER:
        result = additive_cipher(text, key1, reverse=reverse)
    elif cipher_str == MULT_CIPHER:
        result = multiply_cipher(text, key2, reverse=reverse)
    elif cipher_str == AFFINE_CIPHER:
        result = affine_cipher(text, key2, key1, reverse=reverse)
    print "result: ", result


if __name__ == "__main__":
    main()

