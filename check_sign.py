"""This module provide util which sign document with El Gamal algorithm.
"""
# -*- coding: utf-8 -*-
import sys

import ciphers.elgamal as el


def _main():

    print(sys.argv)
    try:
        filename = sys.argv[1]
        a, b, p, g, y = (int(i) for i in sys.argv[2:7])
    except:
        print("check program usage")
        return

    try:
        with open(filename, "r") as f:
            document = f.read()
    
        true_sign = el.check_sign(document, a, b, p, g, y)
        print("This sign is {}valid.".format("" if true_sign else "not "))

    except Exception as error:
        import traceback
        traceback.print_exc()
        print(error)


if __name__ == "__main__":
    _main()
