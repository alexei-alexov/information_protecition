import re


class Swaper(object):

    def __init__(self, key=[3, 1, 4, 5, 2]):
        if isinstance(key, str):
            key = self._parse_key(key)
        
        key = [k - 1 for k in key]
        for n, i in enumerate(sorted(key)):
            if n != i:
                raise ValueError("Wrong key! {}".format(key))
        self.key = key
        self.l = len(key)

    def _parse_key(self, data):
        pat = re.compile("[\D]*")
        print(pat.split(data))
        return [int(i) for i in pat.split(data)]

    def _encode_block(self, block):
        new_block = []
        for k in self.key:
            new_block.append(block[k])
        return "".join(new_block)

    def _decode_block(self, block):
        new_block = [None] * self.l
        for n, c in enumerate(block):
            new_block[self.key[n]] = c
        return "".join(new_block)

    def encode_data(self, data):
        encoded_data = []
        if len(data) % self.l:
            data += 'X' * (self.l - (len(data) % self.l))
        h = len(data) // self.l

        for i in range(0, len(data), self.l):
            encoded_data.append(self._encode_block(data[i:i+self.l]))

        result = []
        for w in range(self.l):
            for i in range(h):
                result.append(encoded_data[i][w])

        return "".join(result)

    def decode_data(self, data):
        h = len(data) // self.l
        d = [data[i:i+h] for i in range(0, len(data), h)]
        encoded_data = "".join(["".join(x) for x in zip(*d)])
        
        new_data = []
        for i in range(0, len(encoded_data), self.l):
            new_data.append(self._decode_block(encoded_data[i:i+self.l]))

        return "".join(new_data)


if __name__ == "__main__":
    s = Swaper(key=[3, 1, 4, 5, 2])

    en = s.encode_data("enemyattackstonight")
    print("encoded: ", en)

    de = s.decode_data(en)
    print("decoded: ", de)
