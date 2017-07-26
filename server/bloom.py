from bitarray import bitarray
import math
import mmh3

class URLFilter:
    def __init__(self, num_items, false_per=0.01):
        temp = -num_items*math.log(false_per) / pow(math.log(2), 2)
        self.size = math.ceil(temp)
        temp = (self.size/num_items) * math.log(2)
        self.runs = math.ceil(temp)

        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)

    def add(self, string):
        for seed in xrange(self.runs):
            result = mmh3.hash(string, seed) % self.size
            self.bit_array[result] = 1

    def lookup(self, string):
        for seed in xrange(self.runs):
            result = mmh3.hash(string, seed) % self.size
            if self.bit_array[result] == 0:
                return 1
            return 0

a = BloomFilter(216553)

