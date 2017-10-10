# -*- coding: utf-8 -*-


class Vigenere(object):
    """The Vigenere Cipher has a key consisting of a word e.g.

    :param key: The keyword, any word or phrase will do. Must consist of alphabetical characters only, no punctuation of numbers.        
    """
    alph = "АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ_"

    def __init__(self,alph="", key=""):
        self.key = (key or 'МОВА').upper()
        self.alph = (alph or self.alph)

    def encipher(self,string):
        """Encipher string using Vigenere cipher according to initialised key. Punctuation and whitespace
        are removed from the input.       
        Example::
            ciphertext = Vigenere('HELLO').encipher(plaintext)     
        :param string: The string to encipher.
        :returns: The enciphered string.
        """           
        string = string.upper()
        print(string)
        print(self.alph, self.key)
        translated = []

        key_index = 0
        
        for symbol in string:
            try:
                
                num = self.alph.index(symbol) + self.alph.index(self.key[key_index])
                num %= len(self.alph)
                translated.append(self.alph[num])
                print(symbol, num)
                key_index += 1
                if key_index == len(self.key):
                    key_index = 0
            except:
                translated.append(symbol)
        return "".join(translated)

    def decipher(self,string):
        """Decipher string using Vigenere cipher according to initialised key. Punctuation and whitespace
        are removed from the input.       
        Example::
            plaintext = Vigenere('HELLO').decipher(ciphertext)     
        :param string: The string to decipher.
        :returns: The enciphered string.
        """               
        string = string.upper()

        translated = []

        key_index = 0
        
        for symbol in string:
            try:
                num = self.alph.index(symbol) - self.alph.index(self.key[key_index])
                num %= len(self.alph)
                translated.append(self.alph[num])
                key_index += 1
                if key_index == len(self.key):
                    key_index = 0
            except:
                translated.append(symbol)
        return "".join(translated)


if __name__ == "__main__":
    v = Vigenere()
    result = v.encipher("ЗАХИСТ_ІНФОРМАЦІЇ")
    print(result)
    print(v.decipher(result))
