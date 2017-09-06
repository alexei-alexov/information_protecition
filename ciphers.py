import string


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
    if reverse:
        func = lambda c: alph[(a_len + alph.find(c) - key) % a_len] if alph.find(c) != -1 else c
    else:
        func = lambda c: alph[(alph.find(c) + key) % a_len] if alph.find(c) != -1 else c
    return cipherer(data, func)



def multiply_cipher(data, key, alph=string.ascii_uppercase, reverse=False):
    a_len = len(alph)
    inv_key1 = find_inverted(key, a_len)
    if reverse:
        func = lambda c: alph[(alph.find(c) * inv_key1) % a_len] if alph.find(c) != -1 else c
    else:
        func = lambda c: alph[(alph.find(c)*key) % a_len] if alph.find(c) != -1 else c
    return cipherer(data, func)


def affine_cipher(data, key1, key2, alph=string.ascii_uppercase, reverse=False):
    a_len = len(alph)
    inv_key1 = find_inverted(key1, a_len)
    if reverse:
        func = lambda c: alph[(inv_key1 * (alph.find(c) - key2)) % a_len] if alph.find(c) != -1 else c
    else:
        func = lambda c: alph[(alph.find(c)*key1 + key2) % a_len] if alph.find(c) != -1 else c
    return cipherer(data, func)


def input(prompt, default_value, validator):
    prompt = "%s\n[%s]> " % (prompt, default_value, )
    while 1:
        value = raw_input(prompt)
        if value == '':return default_value
        try:
            return validator(value)
        except ValueError, err:
            print err


if __name__ == "__main__":
    key1 = 8
    key2 = key1 + 3

    def positive_int_validator(n):
        try:
            n = int(n)
            if n < 1:raise ValueError("Number must be greater than 0")
            return n
        except:
            raise ValueError("Error parsing number. Check input please!")

    def boolean_validator(n):
        n = n.lower()
        if n in ['true', 'y', 'yes', 'tak', 'sure', 't']:
            return True
        if n in ['false', 'n', 'no', 'ni', 'not sure', 'f']:
            return False
        raise ValueError("Wrong value!")
    
    def not_empty_validator(n):
        return n.upper()

    def cipher_validator(n):
        if n in CIPHERS:
            return n
        else:
            raise ValueError("Wrong cipher!")

    key1 = input("Enter key1 please", key1, positive_int_validator)
    key2 = input("Enter key2 please", key2, positive_int_validator)
    
    reverse = input("Reverse?", False, boolean_validator)
   
    cipher_prompt = "Cipher type:\n%s - additive cipher\n%s - multiplicative cipher\n%s - affine_cipher\n" % (
            ADD_CIPHER, MULT_CIPHER, AFFINE_CIPHER, )
    
    cipher_str = input(cipher_prompt, ADD_CIPHER, cipher_validator)
    text = input("Enter data to encrypt / decrypt: ", "test string", not_empty_validator)
    if cipher_str == ADD_CIPHER:
        print "result: ", additive_cipher(text, key1, reverse=reverse)
    elif cipher_str == MULT_CIPHER:
        print "result: ", multiply_cipher(text, key2, reverse=reverse)
    elif cipher_str == AFFINE_CIPHER:
        print "result: ", affine_cipher(text, key2, key1, reverse=reverse)
    add_result = additive_cipher("test string".upper(), key1)
    reverse_add_result = additive_cipher(add_result, key1, reverse=True)

    mult_result = multiply_cipher("test string".upper(), key2)
    reverse_mult_result = multiply_cipher(mult_result, key2, reverse=True)

    affine_result = affine_cipher("test string".upper(), key2, key1)
    reverse_affine_result = affine_cipher(affine_result, key2, key1, reverse=True)
