import binascii
import sys


def string_xor_in_bytes(a, b):
    return [chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)]


def string_xor(a, b):
    return "".join(string_xor_in_bytes(a, b))


if __name__ == "__main__":
    print(string_xor_in_bytes('Hello World', 'Hello World'))
    print(string_xor('Hello World', 'Hello World'))


'''
from os import urandom
import numpy
from numpy import frombuffer, bitwise_xor, byte, fromstring
import time
'''

'''
https://stackoverflow.com/questions/2119761/simple-python-challenge-fastest-bitwise-xor-on-data-buffers
'''
'''
def slow_xor(aa, bb):
    a = frombuffer(aa, dtype=byte)
    b = frombuffer(bb, dtype=byte)
    c = bitwise_xor(a, b)
    r = c.tostring()
    return r


def faster_slow_xor(aa, bb):
    b = fromstring(bb, dtype=numpy.uint64)
    bitwise_xor(frombuffer(aa, dtype=numpy.uint64), b, b)
    return b.tostring()


def simple_tests():
    x1 = bytes('abcdefg', 'utf-8')
    x2 = bytes('abcdefg', 'utf-8')
    y1 = frombuffer(x1, dtype=byte)
    y2 = frombuffer(x2, dtype=byte)
    z1 = bitwise_xor(y1, y2)
    z2 = z1.tostring()
    print('x1:', x1, '..x2:', x2, '..y1:', y1, '..y2:', y2, '..z1', z1, '..z2', z2)


def test_slow_xor(aa, bb):
    for x in range(1000):
        slow_xor(aa, bb)


if __name__ == "__main__":
    simple_tests()

    aa = urandom(2 ** 20)
    bb = urandom(2 ** 20)
    # print('aa:', aa, '.bb:', bb)

    a = time.time()
    test_slow_xor(aa, bb)
    b = time.time()
    print('time:', b - a)
'''

