"""This module provide util which sign document with El Gamal algorithm.
"""
# -*- coding: utf-8 -*-
import sys

import ciphers.elgamal as el


def _main():

    print(sys.argv)
    try:
        filename = sys.argv[1]
        p, g, x = (int(i) for i in sys.argv[2:5])
    except:
        print("check program usage")
        return

    try:
        y = sys.argv[5]
    except:
        y = None

    

    try:
        with open(filename, "r") as f:
            document = f.read()
    
        signer = el.ElGamal(p, g, x, y)
        key = signer.sign(document)
        print("Sign: ({}, {})".format(*key))

    except Exception as error:
        import traceback
        traceback.print_exc()
        print(error)


if __name__ == "__main__":
    _main()
