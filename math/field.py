# Galois Field
# Prime Fields: n = 1
# Extension Fields: n > 1
class gf:
    def __init__(self, p, n):
        self.p = p  # p=a prime
        self.n = n  # n=an integer
    
    def __str__(self):
        return "GF(" + str(self.p) + "," + str(self.n) + ")"
 
    def add(self, a, b):
        return (a + b) % self.p

    def sub(self, a, b):
        return (a - b) % self.p
    
    def mul(self, a, b):
        return (a * b) % self.p
    
    def inverse(self, a):
        pass

if __name__ == "__main__":
    g = gf(2, 8)