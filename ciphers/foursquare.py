# -*- coding: utf-8 -*-


class Foursquare(object):
    """The Foursquare Cipher enciphers pairs of characters, the key consists of 2 keysquares, each 25 characters in length.
    
    :param key1: The first keysquare, as a 25 character string.
    :param key2: The second keysquare, as a 25 character string.
    """
    def __init__(self, key1=None, key2=None, symbol=None):
        self.key1 = key1 or 'Ч ВІПОКЙДУГШЗЄФЛЇХА,ЮРЖЩНЦБИТЬ.СЯМЕ'
        self.key2 = key2 or 'ЕЛЦЙП.ХЇАНШДЄКСІ БФУЯТИЧГМО,ЖЬВЩЗЮР'
        print(self.key1, self.key2)
        self.symbol = symbol or 'Х'
        self.w = 5
        self.h = len(self.key1) // self.w
        
    def get_key1_index(self, c):
        """Return pair x, y of given character"""
        return self.key1.index(c)%self.w, self.key1.index(c)//self.w

    def get_key2_index(self, c):
        """Return pair x, y of given character"""
        return self.key2.index(c)%self.w, self.key2.index(c)//self.w

    def encipher_pair(self,a,b):
        print("pair: ", a, b)
        ax, ay = self.get_key1_index(a)
        bx, by = self.get_key2_index(b)
        if ay == by:
            return self.key2[by*self.w+ax] + self.key1[ay*self.w+bx]
        else:
            return self.key2[ay*self.w+bx] + self.key1[by*self.w+ax]
        
    def decipher_pair(self,a,b):
        ax, ay = self.get_key2_index(a)
        bx, by = self.get_key1_index(b)       
        if ay == by:
            return self.key1[by*self.w+ax] + self.key2[ay*self.w+bx]
        else:
            return self.key1[ay*self.w+bx] + self.key2[by*self.w+ax]

    def encipher(self,string):
        """Encipher string using Foursquare cipher according to initialised key.

        Example::
            ciphertext = Foursquare(key1='zgptfoihmuwdrcnykeqaxvsbl',key2='mfnbdcrhsaxyogvituewlqzkp').encipher(plaintext)     
        :param string: The string to encipher.
        :returns: The enciphered string.
        """
        if len(string)%2 == 1: string += ' '
        ret = []
        for c in range(0,len(string),2):
            ret.append(self.encipher_pair(string[c],string[c+1]))
        return "".join(ret)

    def decipher(self,string):
        """Decipher string using Foursquare cipher according to initialised key. Punctuation and whitespace
        are removed from the input. The ciphertext should be an even number of characters. If the input ciphertext is not an even number of characters, an 'X' will be appended.
        Example::
            plaintext = Foursquare(key1='zgptfoihmuwdrcnykeqaxvsbl',key2='mfnbdcrhsaxyogvituewlqzkp').decipher(ciphertext)     
        :param string: The string to decipher.
        :returns: The deciphered string.
        """
        if len(string)%2 == 1: string = string + ' '
        ret = ''
        for c in range(0,len(string.upper()),2):
            a,b = self.decipher_pair(string[c],string[c+1])
            ret += a + b
        return ret  


if __name__ == "__main__":
    f = Foursquare()
    result = f.encipher(('ПРИЇЗДЖАЮ ШОСТОГО').upper())
    print(result)
    print(f.decipher(result))
    
