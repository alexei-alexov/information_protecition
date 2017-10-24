# -*- coding: utf-8 -*-
from datetime import datetime
import random
import time

from ciphers.primer import get_prime, is_relatively_prime


def _get_random_high():
    """Return big random number"""
    return int(datetime.now().microsecond * datetime.now().microsecond * (1+ random.random()))
    
    
def get_generate_prime_pair(start=1000, end=9999):
    """Return two prime numbers in given range"""
    delta = end - start
    mc = start + _get_random_high() % delta

    first_number = get_prime(mc)

    mc = start + _get_random_high() % delta

    second_number = get_prime(mc)
    if first_number == second_number:
        second_number = get_prime(first_number - 1)

    return (first_number, second_number)


def _get_e(n, d, euler):
    return (n*euler + 1) / d

def generate_rsa_keys(prime_lenth=4):
    """Return tuple of (open, close, mod)"""
    start = 10 ** (prime_lenth-1)
    end = (10 ** (prime_lenth)) - 1
    p, q = get_generate_prime_pair(start=start, end=end)
    n = p * q
    
    print("p: {} q: {}".format(p, q))
    print("n: {}".format(n))

    euler = (p - 1)*(q - 1)

    print("euler function: {}".format(euler))

    d = euler
    while not is_relatively_prime(d, euler):
        d = int(random.random() * (euler-1))
    print("d: {}".format(d))
    
    a = 1
    e = _get_e(a, d, euler)
    while not e.is_integer():
        a += 1
        e = _get_e(a, d, euler)
    e = int(e)
    print("e: {}, d: {}, euler: {}".format(e, d, euler))
    return (e, d, n)
    

def _encode(data, key, mod):
    block_size = len(str(key) - 1)
    pass


class RSA(object):
    """RSA Cipherer"""

    def __init__(self, keys=None):
        if keys:
            self.e, self.d, self.n = keys
        else:
            gen_keys()

    def gen_keys():
        self.p, self.q = get_generate_prime_pair()
        self.n = self.p * self.q
        
        print("p: {} q: {}".format(self.p, self.q))
        print("n: {}".format(self.n))

        self.euler = (self.p - 1)*(self.q - 1)

        print("euler function: {}".format(self.euler))

        self.d = self.euler
        while not is_relatively_prime(self.d, self.euler):
            self.d = int(random.random() * (self.euler-1))
        print("d: {}".format(self.d))
        
        a = 1
        self.e = _get_e(a, self.d, self.euler)
        while not self.e.is_integer():
            a += 1
            self.e = _get_e(a, self.d, self.euler)
        self.e = int(self.e)
        print("e: {}, d: {}, euler: {}".format(self.e, self.d, self.euler))

    def encode_file(self, filename, encoded_filename=None):
        if not encoded_filename:
            encoded_filename = "enc_" + filename
        try:
            with open(filename, 'rb') as f, open(encoded_filename, 'wb') as e:
                for raw_c in f:
                    e.write(chr((int(raw_c)+self.e) % self.n))
        except Exception as e:
            print(e)


    def encode(self, data):
        encoded = []
        for c in data:
            pass

    def decode(self, data):
        pass



def main():
    pass

if __name__ == "__main__":
    
    #r = RSA()
    print(generate_rsa_keys())

