# -*- coding: utf-8 -*-
import hashlib
import random

from ciphers.primer import get_prime


def generate_key(size=6):
    """Generate all keys we need to encrypt hash"""
    min_p, max_p = 10**(size-1), 10**size
    p = get_prime(random.randint(min_p, max_p))
    g = get_prime(random.randint(3, p-1))
    x = random.randint(2, p)
    y = pow(g, x, p)
    return (p, g, x, y)


def is_relatively_prime(a, b):
    """Return True if numbers are relatively prime"""
    while a != b: a, b = (a - b, b) if a > b else (a, b - a)
    return a == 1


def get_hash(payload, p):
    """Return hash of give payload"""
    hasher = hashlib.md5()
    hasher.update(payload.encode())
    return int(hasher.hexdigest(), 16) % p


def check_sign(payload, a, b, p, g, y):
    payload_hash = get_hash(payload, p)
    left_part = (pow(y, a, p) * pow(a, b, p)) % p
    right_part = pow(g, payload_hash, p)
    return left_part == right_part


class ElGamal(object):

    def __init__(self, p, g, x, y=None):
        """
        p and g - open parts.
        x - secret part.
        """
        self.p, self.g, self.x = p, g, x
        self.y = y or pow(g, x, p)

    def _gen_b(self, a, k):
        b = 1
        xa = self.x*a
        pmo = self.p - 1
        while (xa + k*b) % pmo != self.payload_hash:
            b += 1
        # print("(xa + k*b) mod p: {} b: {}".format((xa + k*b) % self.p, b))
        return b

    def sign(self, payload):
        self.payload_hash = get_hash(payload, self.p)
        # print("hash: {}".format(self.payload_hash))

        p_dec = self.p - 1
        k = p_dec
        while not is_relatively_prime(k, p_dec):
            k = random.randint(1, p_dec-1)
        a = pow(self.g, k, self.p)
        b = self._gen_b(a, k)
        # print("k: {} (a: {} b: {})".format(k, a, b))
        return (a, b)

if __name__ == "__main__":
    import sys

    m = "baaqab"
    m2 = "baaqab2"
    try:
        key_size = int(sys.argv[1])
    except:
        key_size = 7
    try:
        tests_amount = int(sys.argv[2])
    except:
        tests_amount = 500
    done = 0
    success = 0

    print("Running El Gamal test.\nAmount of tests: {} key size: {}".format(tests_amount, key_size))
    
    for _ in range(tests_amount):
        done += 1
        p, g, x, y = generate_key(key_size)
        
        el = ElGamal(p, g, x)
        sign_key = el.sign(m)

        try:
            true_valid = check_sign(m, *sign_key, p, g, y)
            assert true_valid
            false_valid = check_sign(m2, *sign_key, p, g, y)
            assert not false_valid
            success += 1
        except:
            print("Fault... {}".format( (p, g, x, y, *sign_key) ))

    print("Testing done. Success: {}% ({} / {})".format(int(success / done * 100), success, done))