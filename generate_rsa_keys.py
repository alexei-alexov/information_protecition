# -*- coding: utf-8 -*-
"""This module generate public and private RSA keys.

Run it from command line.
Result will be in build/ folder
"""
import sys
import os

from ciphers import rsa


RESULT_DIR = "build/"
PUBLIC_KEY_FILE = "public.rsa"
PRIVATE_KEY_FILE = "private.rsa"


def _main():

    try:
        os.mkdir(RESULT_DIR)
    except FileExistsError as error:
        pass

    if len(sys.argv) != 2:
        key_len = 4
    else:
        key_len = int(sys.argv[1])

    public, private, big_n = rsa.generate_rsa_keys(prime_lenth=key_len)

    with open(RESULT_DIR + PUBLIC_KEY_FILE, 'w') as output_file:
        output_file.write(str(public))
        output_file.write("\n")
        output_file.write(str(big_n))

    with open(RESULT_DIR + PRIVATE_KEY_FILE, 'w') as output_file:
        output_file.write(str(private))
        output_file.write("\n")
        output_file.write(str(big_n))


if __name__ == "__main__":
    _main()
