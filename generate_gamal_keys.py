import sys

from ciphers.elgamal import generate_key


if __name__ == "__main__":
    
    try:
        key_size = int(sys.argv[1])
    except:
        key_size = 6


    p, g, x, y = generate_key(key_size)
    print("Keys are generated: p - {} g - {} x - {} y - {}".format(p, g, x, y))