# -*- coding: utf-8 -*-
"""This module contains playfair and double square ciphers."""
import re


DOUBLE_SQUARE_KEY1 = (
    ('Ч', ' ', 'В', 'І', 'П'),
    ('О', 'К', 'Й', 'Д', 'У'),
    ('Г', 'Ш', 'З', 'Є', 'Ф'),
    ('Л', 'Ї', 'Х', 'А', ','),
    ('Ю', 'Р', 'Ж', 'Щ', 'Н'),
    ('Ц', 'Б', 'И', 'Т', 'Ь'),
    ('.', 'С', 'Я', 'Ь', 'Е'),
)

DOUBLE_SQUARE_KEY2 = (
    ('Е', 'Л', 'Ц', 'Й', 'П'),
    ('.', 'Х', 'Ї', 'А', 'Н'),
    ('Ш', 'Д', 'Є', 'К', 'С'),
    ('І', ' ', 'Б', 'Ф', 'У'),
    ('Я', 'Т', 'И', 'Ч', 'Г'),
    ('М', 'О', ',', 'Ж', 'Ь'),
    ('В', 'Щ', 'З', 'Ю', 'Р'),
)

class Playfair(object):
    """The Playfair Cipher enciphers pairs of characters, the key consists of a keysquare 25 characters in length.
    
    :param key: The keysquare, as a 25 character string.
    """
    punctuation_pattern = re.compile('[^\w]', re.UNICODE)

    def __init__(self, key=None, symbol=None):
        self.key = key or 'LGDBAQMHECURNIFXVSOKZYWTP'
        self.symbol = symbol or 'X'

    def remove_punctuation(self, text, filter=r'[\S]'):
        return self.punctuation_pattern.sub('', text.upper())

    def care_of_dublicates(self, text):
        pattern = r"(.)\1"
        replace_pattern = r"\1{}\1".format(self.symbol)
        return re.sub(pattern, replace_pattern, re.sub(pattern, replace_pattern, text))
        
    def encipher_pair(self, a, b):
        arow, acol = int(self.key.index(a) / 5), self.key.index(a) % 5
        brow, bcol = int(self.key.index(b) / 5), self.key.index(b) % 5
        if arow == brow:
            return self.key[arow * 5 + (acol + 1) % 5] + self.key[brow * 5 + (bcol + 1) % 5]
        elif acol == bcol:
            return self.key[((arow + 1) % 5) * 5 + acol] + self.key[((brow + 1) % 5) * 5 + bcol]
        else:
            return self.key[arow * 5 + bcol] + self.key[brow * 5 + acol]
        
    def decipher_pair(self, a, b):
        assert a != b, 'two of the same letters occurred together, illegal in playfair'
        arow, acol = int(self.key.index(a) / 5), self.key.index(a) % 5
        brow, bcol = int(self.key.index(b) / 5), self.key.index(b) % 5
        if arow == brow:
            return self.key[arow * 5 + (acol - 1) % 5] + self.key[brow * 5 + (bcol - 1) % 5]
        elif acol == bcol:
            return self.key[((arow - 1) % 5) * 5 + acol] + self.key[((brow - 1) % 5) * 5 + bcol]
        else:
            return self.key[arow * 5 + bcol] + self.key[brow * 5 + acol]
        
    def encipher(self, string):
        """Encipher string using Playfair cipher according to initialised key. Punctuation and whitespace
        are removed from the input. If the input plaintext is not an even number of characters, an 'X' will be appended.
        Example::
            ciphertext = Playfair(key='zgptfoihmuwdrcnykeqaxvsbl').encipher(plaintext)     
        :param string: The string to encipher.
        :returns: The enciphered string.
        """    
        string = self.remove_punctuation(string)  
        string = re.sub(r'[J]', 'I', string)
        string = self.care_of_dublicates(string)
        if len(string) % 2 == 1:
            string += self.symbol

        try:
            ret = []
            for c in range(0, len(string), 2):
                ret += self.encipher_pair(string[c], string[c + 1])
            return "".join(ret)
        except:
            return "Error in key? Couldn't find symbol!"

    def decipher(self, string):
        """Decipher string using Playfair cipher according to initialised key. Punctuation and whitespace
        are removed from the input. The ciphertext should be an even number of characters. If the input ciphertext is not an even number of characters, an 'X' will be appended.
        Example::
            plaintext = Playfair(key='zgptfoihmuwdrcnykeqaxvsbl').decipher(ciphertext)     
        :param string: The string to decipher.
        :returns: The deciphered string.
        """    
        string = self.remove_punctuation(string)
        if len(string) % 2 == 1:
            string += self.symbol

        try:
            ret = []
            for c in range(0, len(string), 2):
                ret += self.decipher_pair(string[c], string[c + 1])
            return "".join(ret)
        except:
            return "Error in key? Couldn't find symbol!"
