# -*- coding: utf-8 -*-
'''
class abc:
    def __init__(self,a):
        self.a = a
    
    def __add__(self, b):
        self.a = self.a + b.a

    def __int__(self):
        return self.a
    
    def __str__(self):
        return str(self.a)
    
    def __mul__(self, b):
        self.a = self.a * b
    
    def m(a, b):
        return a+b

if __name__ == "__main__":
    x = abc(1)
    y = abc(2)
    x+y
    print (x)
    x+=y
    print (x)
    print(abc.m(1,2))
'''

s = "ab测试字符cd".decode("utf-8").encode("utf-8")
b = bytearray(s)
print len(s)
print b
print "".join([chr(x) for x in b])
