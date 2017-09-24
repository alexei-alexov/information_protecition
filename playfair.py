# -*- coding: utf-8 -*-
"""This module contains playfair and double square ciphers."""
import re


PLAYFAIR_KEY = (
    ('L', 'G', 'D', 'B', 'A'),
    ('Q', 'M', 'H', 'E', 'C'),
    ('U', 'R', 'N', 'I', 'F'),
    ('X', 'V', 'S', 'O', 'K'),
    ('Z', 'Y', 'W', 'T', 'P'),
)

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

PLAYFAIR_SYMBOL = 'X'

def matrix_index(c, key):
    """Return x and y of element on key matrix.
    
    If matrix doesn't contain character - return (-1, -1)

    Arguments:
        c -- character to find.
        key -- 2D key matrix.
    """

    for row_n, row in enumerate(key):
        try:
            return (row.index(c), row_n,)
        except: pass
    return (-1, -1)

def prepare_data(data, symbol=PLAYFAIR_SYMBOL):
    """Prepare data to be correctly encrypted.
    
    Add symbol between repeating letters.
    Example: gg -> gxg
    Make data length pair.
    """
    pattern = r"(.)\1"
    replace_pattern = r"\1{}\1".format(symbol)
    data = re.sub(pattern, replace_pattern, re.sub(pattern, replace_pattern, data))
    return data+symbol if (len(data) & 1) else data


def playfair(data, reverse=False, sumbol=PLAYFAIR_SYMBOL, key=PLAYFAIR_KEY):
    def matrix_index(c):
        return matrix_index(c, key)
    
    data = prepare_data(data)
    pairs = [data[n:n+2] for n in xrange(0, len(data), 2)]

    for left, right in pairs:
        pass
        
    return ""
    
