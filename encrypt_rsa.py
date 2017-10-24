"""This module provide util which encode with RSA given key

Usage:
$py encrypt_rsa.py <file_to_encrypt> <target_file> <path_to_key>
"""
# -*- coding: utf-8 -*-
import sys

from ciphers import rsa


BITS_IN_BYTE = 8
BYTE_ORDER = 'big'


MODE_ENCRYPT = "-e"
MODE_DECRYPT = "-d"


def get_size_in_bytes(i):
    b = 0
    while i > 0:
        i >>= 1
        b += 1       
    return b // BITS_IN_BYTE


def _main():
    if len(sys.argv) != 5:
        print("check program usage")
        return

    _, mode_key, source_file, target_file, key_file = sys.argv


    if mode_key == MODE_ENCRYPT:
        is_encrypt = True
    elif mode_key == MODE_DECRYPT:
        is_encrypt = False
    else:
        print("Wrong key")
        return

    try:
        with open(key_file, "r") as f:
            encode_key = int(f.readline())
            big_key = int(f.readline())
            print("encode_key: {} big_key: {}".format(encode_key, big_key))

        print("loaded key")
        
        key_bytes = get_size_in_bytes(big_key)

        # this is done, to avoid problems with program!
        if is_encrypt:
            read_chunk_size = key_bytes - 1
            write_chunk_size = key_bytes + 1
        else:
            read_chunk_size = key_bytes + 1
            write_chunk_size = key_bytes - 1


        print("bytes size: {}".format(key_bytes))
        
        with open(source_file, "rb") as input_file:
            with open(target_file, "wb") as output_file:
                while True:
                    chunk = input_file.read(read_chunk_size)
                    if not chunk: break
                    num =  int.from_bytes(chunk, BYTE_ORDER)
                    encrypted_num = pow(num, encode_key, big_key)
                    encrypted_chunk = encrypted_num.to_bytes(write_chunk_size, BYTE_ORDER)
                    #print("{} -> {} -> {} -> {}".format(chunk, num, encrypted_num, encrypted_chunk))
                    if num >= big_key:
                        print("CANCER")
                        break
                    
                    output_file.write(encrypted_chunk)
    except Exception as error:
        import traceback
        traceback.print_exc()
        print(error)


if __name__ == "__main__":
    _main()
